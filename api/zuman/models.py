from datetime import datetime
from secrets import token_hex

from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

from zuman import db, login_manager
from zuman.utils import create_str


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


default_pic = "zuman.jpg"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    image_file = db.Column(db.String(50), nullable=False, default=default_pic)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    sid = db.Column(db.String(36), nullable=False, unique=True, default='no_login' + token_hex(14))

    def get_reset_token(self):
        s = Serializer(current_app.config["SECRET_KEY"], current_app.config['SALT'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"], current_app.config['SALT'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return create_str(self, ['_sa_instance_state', 'password'])


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_accessed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.content}')"
