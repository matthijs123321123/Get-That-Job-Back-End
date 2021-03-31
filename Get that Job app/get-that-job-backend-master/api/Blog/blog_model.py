from api import db
from datetime import datetime 
from api.Tags_blog.tag_blog_table import tag_blog

class Blog(db.Model):
    """Class model for the blog table"""
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    feature_image = db.Column(db.String,nullable=True)
    tags = db.relationship('Tag',secondary=tag_blog,backref=db.backref('blogs_associated',lazy="dynamic"))
    
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'content' : self.content,
            'creation_date' : self.creation_date,
            'feature_image' : self.feature_image
        }



