from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.BigInteger)
    roll = db.Column(db.Integer, unique=True)
    address = db.Column(db.String(100))
    college = db.Column(db.String(100))

    def __init__(self, name, phone, roll, address, college):
        self.name = name
        self.phone = phone
        self.roll = roll
        self.address = address
        self.college = college

    def __repr__(self):
        return f"<Student {self.name}>"