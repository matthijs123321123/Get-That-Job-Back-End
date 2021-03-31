from flask import Blueprint,request,jsonify
from api.User.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required
from api import db

user=Blueprint('User',__name__)

@user.route('/adduser', methods=["POST"])
def adduser():
    request_data = request.get_json()

    user=User.query.filter_by(email=request_data["email"]).first()
    if user:
        return "Email already registered", 400
    else:
        password_hash=request_data["password"]
        new_user=User(email=request_data["email"],password=request_data["password"],role=2)
        new_user.password = generate_password_hash(new_user.password,'sha256',salt_length=12)
        db.session.add(new_user)
        db.session.commit()
        
        return "user added", 200


        