from flask import Flask
from config.config import Config
from db.database import db
from sqlalchemy import inspect
import os
from flask_jwt_extended import JWTManager 
from flask_migrate import Migrate 
from services.error_handler import handle_error 

jwt = JWTManager()  
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)  
    migrate.init_app(app, db) 

    from app.models import User

    if not os.getenv("WERKZEUG_RUN_MAIN"):  
        with app.app_context():
            inspector = inspect(db.engine)
            existing_tables = inspector.get_table_names()
            if not existing_tables:
                print("Creating tables...")
                db.create_all()
            else:
                print("Tables already exist.")

    from app.routes import auth 
    app.register_blueprint(auth, url_prefix='/auth')  
    app.register_error_handler(Exception, handle_error)

    return app
