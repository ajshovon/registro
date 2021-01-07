from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class StudentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), nullable=False)
    student_name = db.Column(db.String(50), nullable=False)
    reg_status = db.Column(db.String(20), nullable=False)
    courses = db.relationship('CoursesData',cascade="all, delete-orphan", backref = 'studentobj')

class CoursesData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(20))
    course_section = db.Column(db.String(20))
    students_id = db.Column(db.Integer, db.ForeignKey('student_data.id'))

db.create_all()
    