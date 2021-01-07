from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

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

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'student_id_s' in request.form:
            search_id = request.form['student_id_s']
            res = StudentData.query.filter_by(student_id=search_id).all()
            if not res:
                return render_template('result404.html', students=res)
            else:
                return render_template('result.html', students=res)
        else:
            new_student_name = request.form['student_name']
            new_student_id = request.form['student_id']
            new_student_reg = request.form['reg_status']
            new_student = StudentData(student_name=new_student_name, student_id=new_student_id, reg_status=new_student_reg)
            new_student_courses = request.form.getlist('course[]')
            new_student_sec = request.form.getlist('section[]')
            l = len(new_student_courses)
            db.session.add(new_student)
            db.session.commit()
            for i in range(l):
                student_course = CoursesData(course_id=new_student_courses[i], course_section = new_student_sec[i], studentobj=new_student)
                db.session.add(student_course)
                db.session.commit()
            return redirect('/')
    else:
        all_students = StudentData.query.order_by(StudentData.student_id).all()
        return render_template('home.html', students=all_students)

@app.route('/delete/<int:id>')
def delete(id):
    select_id = StudentData.query.get_or_404(id)
    db.session.delete(select_id)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    edit_student = StudentData.query.get_or_404(id)
    if request.method == 'POST':
        edit_student.student_name = request.form['student_name_']
        edit_student.student_id = request.form['student_id_']
        edit_student.reg_status = request.form['reg_status_']
        db.session.commit()
        return redirect('/')
    else:
        all_students = StudentData.query.order_by(StudentData.student_id).all()
        return render_template('edit2.html', student=edit_student, students=all_students)


@app.route('/view/<int:id>', methods=['GET', 'POST'])
def view(id):
    view_student = StudentData.query.get_or_404(id)
    all_students = StudentData.query.order_by(StudentData.student_id).all()
    return render_template('view.html', viewstudent=view_student, students=all_students)


if __name__ == '__main__':
  app.run()

