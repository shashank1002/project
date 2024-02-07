from flask import Blueprint, request
from controller import update_data, get_id, get_student, delete_data, get_json

blueprint_update = Blueprint('blueprint_update', __name__)

@blueprint_update.route('/student/<student_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_student(student_id):
    student = get_student(student_id)
    if request.method == 'GET':
        response = get_id(student)
        delete_data(student)
        return {"message": "success", "student": response}

    elif request.method == 'PUT':
        data = get_json()
        update_data(data, student)
        return {"message": f"Student {student.name} successfully updated"}

    elif request.method == 'DELETE':
        delete_data(student)
        return {"delete": f"Student {student.name} deleted successfully"}