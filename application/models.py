from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(128), nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)

	def get_reset_token(self, expires_seconds=1800):
		s = Serializer(current_app.config['SECRET_KEY'], expires_seconds)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])

		try:
			user_id = s.loads(token)['user_id']
		except:
			return None

		return Users.query.get(user_id)

	def __repr__(self):
		return ''.join(["User('{self.username}', '{self.email}', '{self.image_file}')"])

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join(["Post('{self.title}', '{self.date_posted}')"])
