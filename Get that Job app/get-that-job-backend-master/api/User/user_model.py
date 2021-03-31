from api import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(120),nullable=False)
    role = db.Column(db.Integer, nullable=True)

    @property
    def serialize(self): 
        return {
            'id' : self.id,
            'email' : self.email,
            'password' : self.password,
            'role' : self.role,
        }
    