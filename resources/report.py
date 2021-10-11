from flask_restful import Resource
from flask import request

from models.db import db
from models.report import Report

from middleware import create_token, strip_token, read_token, compare_password, gen_password

#grabs all reports and creates report
class Reports(Resource):
    def get(self):
        raw_reports = Report.find_all_reports()
        reports = [report.json() for report in raw_reports]
        return reports

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        report = Report(**params)
        report.create()
        return report.json(), 201


#updates and deletes report
class report_by_id(Resource):
    def put(self, id):
        data = request.get_json()
        token = strip_token(request)
        payload = read_token(token)
        if payload:
            report = Report.find_report_by_id(id)
            if payload["id"] == report["user_id"]:
                for key in data.keys():
                    report[key] = data[key]
                db.session.commit()
                return report.json(), 200
            return {"msg": "Unauthorized credentials"}, 404
        return {"msg": "Unauthorized access"}, 404

    def delete(self, id):
        token = strip_token(request)
        payload = read_token(token)
        if payload:
            report = Report.find_report_by_id(id)
            if payload["id"] == report["user_id"]:
                db.session.delete(report)
                db.session.commit()
                return {"msg": "report deleted!", "payload": report.id}, 200
            return {"msg": "Unauthorized credentials"}, 404
        return {"msg": "Unauthorized access"}, 404


#handles reports of ProjectDetail page
class report_by_project_id(Resource):
    def get(self, project_id):
        raw_reports = Report.find_reports_by_project_id(project_id)
        reports = [report.json() for report in raw_reports]
        return reports, 200
