from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import click
from flask.cli import with_appcontext
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash


db = SQLAlchemy()



def create_app():
    """Creates flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
    app.config['SQLALCHEMY_track_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)
    app.config["CLIENT_IMAGES"] = 'api\Blog\images'
    app.config['JWT_SECRET_KEY']='YOUR_SECRET_KEY'
    jwt=JWTManager(app)

    from api.Blog.blog_routes import blogs
    app.register_blueprint(blogs)

    from api.User.user_model import User

    from api.User.user_route import user
    app.register_blueprint(user)

    from api.Login.login_route import login
    app.register_blueprint(login)



    @click.command(name='create_admin')
    @with_appcontext
    def create_admin():
        admin=User(email="admin_email_address",password="admin_password",role=0)
        admin2=User(email="Test_Admin",password="123123",role=1)
        admin3=User(email="Test_User",password="123123",role=2)
        admin.password = generate_password_hash(admin.password,'sha256',salt_length=12)
        admin2.password = generate_password_hash(admin2.password,'sha256',salt_length=12)
        admin3.password = generate_password_hash(admin3.password,'sha256',salt_length=12)
        db.session.add(admin)
        db.session.add(admin2)
        db.session.add(admin3)
        db.session.commit()
    
    app.cli.add_command(create_admin)

    return app