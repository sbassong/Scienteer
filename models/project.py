from datetime import datetime
from models.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)

    #associations
    reports = db.relationship('Report', backref=db.backref('project_reports', lazy=True))
    user = db.relationship('User', backref=db.backref('project_researcher', lazy=True))


    def __init__(self, title, category, requirements, instructions, user_id):
        self.title = title
        self.category = category
        self.requirements = requirements
        self.instructions = instructions
        self.user_id = user_id
        

    def json(self):
        return {"id": str(self.id), "title": self.title, "user_id": str(self.user_id), "category": self.category, "instructions": self.instructions, "requirements": self.requirements, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self.json()

    @classmethod
    def find_all_projects(cls):
        return Project.query.all()

    @classmethod
    def find_project_by_id(cls, id):
        project = Project.query.filter_by(id=id).first_or_404()
        return project

    @classmethod
    def find_projects_by_user_id(cls, user_id):
        projects = Project.query.filter_by(user_id=user_id).all()
        return projects

    @classmethod
    def find_projects_by_category(cls, category):
        projects = Project.query.filter_by(category=category).all()
        return projects
