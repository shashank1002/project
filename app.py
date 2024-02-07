from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from controller_add import blueprint_get
from controller_update import blueprint_update
from model import db  # Import the SQLAlchemy instance

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\HR\\country.db"
db.init_app(app)  
migrate = Migrate(app, db)

app.register_blueprint(blueprint_get)
app.register_blueprint(blueprint_update)

if __name__ == "__main__":
    app.run(debug=True)