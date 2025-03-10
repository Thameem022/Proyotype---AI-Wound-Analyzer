from app.models import User
from db.database import db
from flask_bcrypt import Bcrypt
from services.validation.user import is_valid_email, is_strong_password

bcrypt = Bcrypt()

def create_user(email, password):
    """ Create a new user with a hashed password, ensuring proper validations """

    if not is_valid_email(email):
        return {"error": "Invalid email format. Please enter a valid email."}, 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"error": "Email already registered. Please use a different email."}, 409

    if not is_strong_password(password):
        return {"error": "Password must be at least 8 characters long and include both letters and numbers."}, 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    
    return {"message": "User registered successfully!"}, 201

def authenticate_user(email, password):
    """ Authenticate user login """
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user.id 
    return None 

def prepare_user_payload(email, password):
    """
    Prepares the user payload for API requests.
    """
    return {"email": email, "password": password}
