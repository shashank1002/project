from app import app
from flask import request
from controller import create, require_data, get_json

@app.route('/student', methods=['POST', 'GET'])
def handle_student():
    if request.method == 'POST':
        if request.is_json:
            data = get_json()
            create(data)
            return {"message": "Student  has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        results = require_data()
        return {"count": len(results), "students": results}