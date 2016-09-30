from flask import Flask, render_template, request
from ConnectionFactory import getConnection
from StudentPopo import Student
from StudentDao import StudentDao

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
            std = Student(request.form)
            stdDao= StudentDao(getConnection())
            return render_template("result.html", msg=stdDao.addStudent(std))


@app.route('/list')
def list():
    stdDao= StudentDao(getConnection())
    return render_template("list.html", rows=stdDao.getListOfStudent())


if __name__ == '__main__':
    app.run(debug=True)
