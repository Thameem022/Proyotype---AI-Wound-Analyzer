from flask import Blueprint, request, jsonify
from modules.user import prepare_user_payload, create_user, authenticate_user 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from services.storage.s3 import upload_image_to_s3
from app.models import Image
from db.database import db

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    print("Signup endpoint hit")  
    data = request.get_json()
    print("Received data:", data)

    user_payload = prepare_user_payload(data['email'], data['password'])
    print("User payload:", user_payload)  

    response = create_user(data['email'], data['password'])
    print("Response from service:", response)

    return jsonify(response), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_payload = prepare_user_payload(data['email'], data['password'])

    user_id = authenticate_user(data['email'], data['password']) 

    if user_id:
        access_token = create_access_token(identity=str(user_id))
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401


@auth.route('/upload', methods=['POST'])
@jwt_required()
def upload_image():
    """Handles image upload and stores metadata in PostgreSQL"""
    user_id = get_jwt_identity() 

    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    response = upload_image_to_s3(file, user_id)

    if "error" in response:
        return jsonify(response), 500 

    new_image = Image(user_id=user_id, image_url=response["file_url"])
    db.session.add(new_image)
    db.session.commit()

    return jsonify({"message": "File uploaded successfully", "url": response["file_url"]}), 201

@auth.route('/images', methods=['GET'])
@jwt_required()
def get_images():
    """Retrieve images uploaded by the authenticated user."""
    user_id = get_jwt_identity()  # Get user ID from JWT

    # Query images belonging to the user
    images = Image.query.filter_by(user_id=user_id).all()

    # Return a list of image URLs
    image_data = [{"id": img.id, "image_url": img.image_url, "upload_time": img.upload_time} for img in images]

    return jsonify(image_data), 200