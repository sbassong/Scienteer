from datetime import datetime
from models.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey('projects.id'), nullable=False)

    #associations
    project = db.relationship('Project', backref=db.backref('report_project', lazy=True))
    user = db.relationship('User', backref=db.backref('report_creator', lazy=True))


    def __init__(self, content, location, image, project_id, user_id):
        self.content = content
        self.location = location
        self.image = image
        self.project_id = project_id
        self.user_id = user_id
        

    def json(self):
        return {"id": str(self.id), "content": self.content, "location": self.location, "image": self.image, "user_id": str(self.user_id), "project_id": str(self.project_id),  "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self.json()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all_reports(cls,):
        return Report.query.all()

    @classmethod
    def find_reports_by_project_id(cls, project_id):
        reports = Report.query.filter_by(project_id=project_id).all()
        return reports

    @classmethod
    def find_reports_by_user_id(cls, user_id):
        reports = Report.query.filter_by(user_id=user_id).all()
        return reports

    @classmethod
    def find_report_by_id(cls, id):
        report = Report.query.filter_by(id=id).first_or_404()
        return report

    @classmethod
    def update(cls, id, fields):
        report = Report.find_report_by_id(id)
        for key in fields:
            setattr(report, key, fields[key])
        db.session.commit()
        return report.json()