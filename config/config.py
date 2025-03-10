import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key') 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback_jwt_key')
    API_BASE_URL = os.getenv('API_BASE_URL', 'http://127.0.0.1:5000/')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_USER = os.getenv('DB_USER', 'wound_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'wound_user')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'wound_analyzer_db')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
