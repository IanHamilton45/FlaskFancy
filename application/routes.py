from flask import render_template, redirect, url_for, flash
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, LoginForm, RegistrationForm

@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	return render_template('home.html', posts=postData)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#Check if email-password correct
		if form.email.data == 'admin@QA.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')

	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.email.data}!', 'success')

		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(email=form.email.data, password=hashed_pw)
		#db.session.add(user)
		#db.session.commit()
		return redirect(url_for('home'))

	return render_template('register.html', title='Register', form=form)
	

@app.route('/post', methods=['GET','POST'])
def post():
	form = PostForm()

	if form.validate_on_submit():
		postData = Posts(
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			title = form.title.data,
			content = form.content.data
			)
		db.session.add(postData)
		db.session.commit()

		return redirect(url_for('home'))
	else:
		print (form.errors)

	return render_template('post.html', title='Post', form=form)
