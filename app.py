from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\HR\\country.db"
db.init_app(app)  
migrate = Migrate(app, db)

import controller_add
import controller_update

if __name__ == "__main__":
    app.run(debug=True)