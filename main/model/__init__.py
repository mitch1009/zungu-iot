"""  
DataBase Management
"""
import enum
import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from main.config import app

db = SQLAlchemy(app)


class ROLES(enum.Enum):
    """ ROLES"""
    USER = "User"
    ADMIN = "Admin"
    SUPERADMIN = "SuperAdmin"
    ACCOUNTS = "Accounts"
    SUPPORT = "Support"


class STATUS(enum.Enum):
    """ Account Status Enum"""
    ACTIVE = "Active"
    DISABLED = "Soft Disable"
    SUSPENDED = "Suspended"
    INSECURE = "Under Security Review"
    PENDING = "Pending"


class Role(db.Model):
    __tablename__ = "Role"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Enum(ROLES, values_callable=lambda obj: [e.value for e in obj]))
    permisions = db.Column(db.String(265))


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.BIGINT, unique=True, nullable=False)
    email = db.Column(db.String(266), unique=True, nullable=False)
    ref = db.Column(db.Integer, db.ForeignKey("User.id"))
    package = db.Column(db.Integer, db.ForeignKey("Package.id"))
    date_reg = db.Column(db.DateTime, default=datetime.now())
    account_number = db.Column(db.String(255), default=uuid.uuid4())
    courses = db.relationship("Course", backref="course_id", lazy=True)
    national_id = db.Column(db.String(266))
    id_type = db.Column(db.String(255))
    status = db.Column(db.Enum(STATUS, values_callable=lambda obj: [e.value for e in obj]), default=STATUS.PENDING)
    role = db.Column(db.Enum(ROLES, values_callable=lambda obj: [e.value for e in obj]), default=ROLES.USER)


class Course(db.Model):
    """Course Table"""

    __tablename__ = "Course"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    sub_title = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("User.id"))
    images = db.Column(db.Text)
    date_reg = db.Column(db.DateTime, default=datetime.now())


class Package(db.Model):
    __tablename__ = "Package"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level_count = db.Column(db.BIGINT)
    reward = db.Column(db.Integer)
    level = db.relationship("User", backref="package_id", lazy=True)
