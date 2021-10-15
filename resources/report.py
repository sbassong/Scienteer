from flask_restful import Resource
from flask import request

from models.db import db
from models.report import Report

from werkzeug.utils import secure_filename
from middleware import create_token, strip_token, read_token, compare_password, gen_password, allowed_file
from aws import upload_file

#grabs all reports and creates report
class Reports(Resource):
    def get(self):
        raw_reports = Report.find_all_reports()
        reports = [report.json() for report in raw_reports]
        return reports

    def post(self):
        data = request.get_json()
        #upload to s3
        file = request.files['image']
        upload_file(file)
        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            uploaded = upload_file(file)
            data['image'] = uploaded

        params = {}
        for k in data.keys():
            params[k] = data[k]
        report = Report(**params)
        report.create()
        return report.json(), 201


#gets, updates, and deletes report
class Report_by_id(Resource):
    def get(self, id):
        report = Report.find_report_by_id(id)
        if report:
            return report.json(), 200
        return 'report not found', 404

    def put(self, id):
        data = request.get_json()
        token = strip_token(request)
        payload = read_token(token)
        if payload:
            report = Report.find_report_by_id(id)
            if payload["id"] == str(report.user_id):
                file = request.files['image']
                upload_file(file)
                if file and allowed_file(file.filename):
                    file.filename = secure_filename(file.filename)
                    uploaded = upload_file(file)
                    data['image'] = uploaded
                for key in data:
                    setattr(report, key, data[key])
                db.session.commit()
                return report.json(), 200
            return {"msg": "Unauthorized credentials"}, 401
        return {"msg": "Unauthorized access"}, 404

    def delete(self, id):
        token = strip_token(request)
        payload = read_token(token)
        if payload:
            report = Report.find_report_by_id(id)
            if payload["id"] == str(report.user_id):
                db.session.delete(report)
                db.session.commit()
                return {"msg": "report deleted!", "payload": str(report.id)}, 200
            return {"msg": "Unauthorized credentials"}, 401
        return {"msg": "Unauthorized access"}, 404


#handles reports of ProjectDetail page
class Report_by_project_id(Resource):
    def get(self, project_id):
        raw_reports = Report.find_reports_by_project_id(project_id)
        reports = [report.json() for report in raw_reports]
        return reports, 200

# class Report_image(Resource):
#     def put(self, report_id):
#         data = request.get_json()
#         image = data.image
#         file = request.files['file']
#         upload_file(file, image)

#         report = Report.find_report_by_id(report_id)
#         report.image = image
#         # setattr(report, report.image, data[report.image])
#         db.session.merge(report)
#         db.session.commit()
#         return {"msg": "Uploaded"}