from flask import Blueprint,request,jsonify,make_response
from flask_jwt_extended import jwt_required
from api import db
from api.Blog.blog_model import Blog
from api.Tag.tag_model import Tag
from datetime import datetime
import base64
import glob
from flask import send_file, send_from_directory, safe_join, abort

blogs = Blueprint('Blogs',__name__)

@blogs.route('/upimages',methods=["POST"])
@jwt_required
def up_img():
    """Takes a images and saves it on the file server"""
    data = request.get_json()
    file_name = data["file_name"]
    file_data = data["file_data"]
    imgdata = base64.b64decode(file_data)
    filename = 'api/Blog/images/' + file_name 
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return "File uploaded"
    
@blogs.route("/getallimg",methods=["GET"])
@jwt_required
def get_all_img():
    """Gets all img locations"""
    list_img = glob.glob("api/Blog/images/*.*")
    return jsonify({"img" : list_img})


@blogs.route("/getimg/<image_name>", methods=["GET"])
@jwt_required
def get_image(image_name):
    try:
        return send_from_directory("api/Blog/images/", filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@blogs.route('/add_blog',methods=["POST"])
@jwt_required
def create_blog():
    """gets json data, checks of tag is alreadyin DB, then adds tag or not and adds blog to DB"""
    data = request.get_json()
    print(data)
    new_blog=Blog(title=data["title"],content=data["content"],feature_image=data["feature_image"], creation_date=datetime.now())

    for tag in data["tags"]:
        present_tag = Tag.query.filter_by(name=tag).first()
        if present_tag is not None:
            present_tag.blogs_associated.append(new_blog)
        elif present_tag is None:
            new_tag =Tag(name=tag)
            new_tag.blogs_associated.append(new_blog)
            db.session.add(new_tag)
        else:
            pass

    db.session.add(new_blog)
    db.session.commit()

    blog_id = getattr(new_blog, "id")
    return jsonify({"id":blog_id})

@blogs.route('/blogs',methods=["GET"])
@jwt_required
def get_all_blogs():
    blogs = Blog.query.all()
    serialized_data = []
    for blog in blogs:
        serialized_data.append(blog.serialize)

    return jsonify({"all_blogs":serialized_data})

@blogs.route('/blog/<int:id>',methods=["GET"])
@jwt_required
def get_single_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    serialized_blog = blog.serialize
    serialized_blog["tags"] = []

    for tag in blog.tags:
        serialized_blog["tags"].append(tag.serialize)

    return jsonify({"single_blog":serialized_blog})

@blogs.route('/update_blog/<int:id>', methods=["PUT"])
@jwt_required
def update_blog(id):
    data = request.get_json()
    blog=Blog.query.filter_by(id=id).first_or_404()

    blog.title = data["title"]
    blog.content = data["content"]
    blog.feature_image=data["feature_image"]

    updated_blog = blog.serialize

    db.session.commit()
    return jsonify({"blog_id":blog.id})

@blogs.route('/delete_blog/<int:id>',methods=["DELETE"])
@jwt_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()

    return jsonify("Blog deleted"), 200


