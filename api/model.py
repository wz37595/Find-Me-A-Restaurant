# database
from api import db
from datetime import datetime

'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
'''


class User(db.Model):
    UserToken = db.Column(db.String(60), primary_key=True)
    UserName = db.Column(db.String(10), unique=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    CreatedDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"User('{self.userName}', '{self.userToken}')"


taskDetail = db.Table('taskDetail',
                      db.Column('TaskToken', db.String(60), db.ForeignKey('task.TaskToken')),
                      db.Column('RestaurantToken', db.String(60), db.ForeignKey('restaurant.RestaurantToken'))
                      )


class Task(db.Model):
    TaskToken = db.Column(db.String(60), primary_key=True)
    CreatedDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    Status = db.Column(db.String(10), nullable=False, default='PENDING')
    Restaurants = db.relationship('Restaurant', secondary=taskDetail, backref=db.backref('Assignee', lazy='dynamic'))


class Restaurant(db.Model):
    RestaurantToken = db.Column(db.String(60), primary_key=True)
    Name = db.Column(db.String(30))
    YelpScore = db.Column(db.Integer)
    OurScore = db.Column(db.Integer)
    ReviewCount = db.Column(db.Integer, default=0)
    URL = db.Column(db.String(60), nullable=False)
    LastUpdateTime = db.Column(db.DateTime)
    CreatedDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    # TODO: AddMore Attributes later
