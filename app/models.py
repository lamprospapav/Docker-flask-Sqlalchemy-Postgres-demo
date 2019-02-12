from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db,login_manager

class User (UserMixin, db.Model):
    """
    Create an User table
    """

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    books = db.relationship('Book', backref='Users',
                                lazy='dynamic')

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

class Book (db.Model):
    """
    Create an Demo object
    
    """
    __tablename__ = 'book'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60),nullable=False,index=True)
    rating = db.Column(db.Float)
    pub_date = db.Column(db.DateTime,default = datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
   
    def __init__(self, name, rating,user_id):
        self.name = name
        self.rating = rating
        self.user_id= user_id
        
    def __repr__(self):
        return '{}'.format(self.name)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
