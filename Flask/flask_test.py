from flask import Flask, request
from student import Student
import os 
app = Flask(__name__)
@app.get('/')
def homePage():
    return "Hello"

@app.post("/add_student")
def add_student():
    request_data = request.json
    
    stu_obj = Student(name = request_data["stu_name"],
    subjects=request_data["stu_subjects"],marks= request_data["stu_marks"])
    write_tofile(stu_obj=stu_obj)
    get_student(stu_obj=stu_obj)
    return request_data

def get_student(stu_obj:Student):
    print(stu_obj.get_name())

def write_tofile(stu_obj:Student):
    print(stu_obj.print_stu())

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), threaded = True)