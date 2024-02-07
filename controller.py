from model import *

from flask import request

def create(data):
    new_student = StudentModel(name=data['name'], phone=data['phone'], roll=data['roll'], address=data['address'], college=data['college'])
    db.session.add(new_student)
    db.session.commit()
    
def get_student(student_id):
    student = StudentModel.query.get(student_id)
    return student


def require_data():
    students = StudentModel.query.all()
    results = [
        {
            "id": student.id,
            "name": student.name,
            "phone": student.phone,
            "roll": student.roll,
            "address": student.address,
            "college": student.college
        } for student in students]
    return results

def update_data(data, student):
    student.name = data['name']
    student.phone = data['phone']
    student.roll = data['roll']
    student.address = data['address']
    student.college = data['college']
    db.session.commit()

def get_id(student):
    response = {
            "name": student.name,
            "phone": student.phone,
            "roll": student.roll,
            "address": student.address,
            "college": student.college
        }
    return response

def delete_data(student):
    db.session.delete(student)
    db.session.commit()

def get_json():
    return request.get_json()