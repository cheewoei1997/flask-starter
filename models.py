from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(8))
    posts = relationship('Post', backref="user", lazy=True)

    def change_name(self, new_name):
        self.name = new_name


    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %s>" % (self.name)

#    class Post(Base):
#        __tablename__ = 'posts'
#        id = Column(Integer, primary_key=True)
#        content = Column(String(120), unique=False)
#        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#
#        def __init__(self, post=None):
#            self.post = post
#
#        def __repr__(self):
#            return "Post updated!"

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    post = Column(String(120), unique=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


    def change_post(self, new_post):
        self.tweet = new_post

    def __init__(self, post=None, user_id=None):
        self.post = post
        self.user_id = user_id

    def __repr__(self):
        return "Post updated!"

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(120), unique=False)

    def change_com(self, new_post):
        self.tweet = new_post

    def __init__(self, post=None):
        self.post = post

    def __repr__(self):
        return "Post updated!"

class LoginTwo(Base):
    __tablename__ = "logintwo"
    id = Column(Integer, primary_key=True)
    Name = Column(String(120), unique=False)
    Email = Column(String(120), unique=False)

    def change_details(self, Name, Email):
        self.Name = Name
        self.Email = Email

    def __init__(self, Name=None, Email=None):
        self.Name = Name
        self.Email = Email

    def __repr__(self):
        return "Login"

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

