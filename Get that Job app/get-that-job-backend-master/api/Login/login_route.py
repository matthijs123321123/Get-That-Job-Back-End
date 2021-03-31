from flask import Blueprint,request,jsonify
from api.User.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

login=Blueprint('login',__name__)

@login.route('/login', methods=["POST"])
def log_in():
    request_data = request.get_json()

    user=User.query.filter_by(email=request_data["email"]).first()
    if User:
        if check_password_hash(user.password ,request_data["password"]):
            if user.role == 1:
                return jsonify({"email":request_data["email"],"role" : "1"})
            elif user.role == 0:
                jwt_token=create_access_token(identity=user.email, expires_delta=False)
                return jsonify({"token":jwt_token})
            elif user.role == 2:
                return jsonify({"email":request_data["email"], "role" : "2"})
            else:
                return "Error; no role", 400
        else:
            return "Error; upassword hashing", 400

    else:
        return "Invalid email or password", 400

    