from models.db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_digest = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text)
    researcher = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)

    #associations
    projects = db.relationship("Project", cascade='all', backref=db.backref('research_projects', lazy=True))
    reports = db.relationship("Report", cascade='all', backref=db.backref('scienteer_reports', lazy=True))

    def __init__(self, name, email, password_digest, bio, researcher):
        self.name = name
        self.email = email
        self.password_digest = password_digest
        self.bio = bio
        self.researcher = researcher

    def json(self):
        return {"id": str(self.id), "name": self.name, "email": self.email, "password_digest": self.password_digest, "bio": self.bio, "researcher": self.researcher, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self.json()

    @classmethod
    def find_user_by_id(cls, id):
        user = User.query.filter_by(id=id).first_or_404()
        return user

    @classmethod
    def find_user_by_email(cls, email):
        user = User.query.filter_by(email=email).first_or_404()
        return user
        
    @classmethod
    def find_all_users(cls):
        users = User.query.all()
        return users

    @classmethod
    def find_all_scienteers(cls):
        scienteers = User.query.filter_by(researcher=True).all()
        return scienteers

    @classmethod
    def find_all_researchers(cls):
        researchers = User.query.filter_by(researcher=False).all()
        return researchers