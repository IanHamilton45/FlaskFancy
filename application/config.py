
class Config:
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@mysql:3306/blog'
	SECRET_KEY = '82fcc1d59465a9b274d13db8441cbc30'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'blog.ianhamilton.noreply'
	MAIL_PASSWORD = 'pass-007-001' # Set EMAIL_USER evironment variable
