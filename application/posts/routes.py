from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from application import db
from application.posts.forms import PostForm
from application.models import Posts
from flask_mail import Message
from application import mail

posts = Blueprint('posts', __name__)

def send_new_post_email(post):
	msg = Message('New Post on Blog', 
			sender='blog.ianhamilton.noreply@gmail.com', 
			recipients=['ian.hamilton@academytrainee.com'])
	msg.body = "New Blog Post."

	#msg.body = f'''BLOG - NEW POST
#New Post By: {post.author}
#Title: {post.title}
#Content: {post.content}

#To view/edit/delete this post goto: {url_for('posts.post', post_id=post.id, _external=True)}
#'''

	mail.send(msg)

@posts.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Posts(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()


		send_new_post_email(post)
		flash('Post created!', 'success')
		return redirect(url_for('main.home'))

	return render_template('create_post.html', title='New Post', 
							legend='Update Post', form=form)

@posts.route('/post/<int:post_id>')
def post(post_id):
	post = Posts.query.get_or_404(post_id)
	return render_template('post.html', title=post.title, post=post)

@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
	post = Posts.query.get_or_404(post_id)
	if post.author != current_user and current_user.email != 'ian.hamilton@academytrainee.com':
		abort(403)

	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash('Post updated successfully.', 'success')
		return redirect(url_for('posts.post', post_id=post.id))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create_post.html', title='Update Post', 
							legend='Update Post', form=form)

@posts.route('/delete_post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
	post = Posts.query.get_or_404(post_id)

	if post.author != current_user and current_user.email != 'ian.hamilton@academytrainee.com':
		abort(403)

	db.session.delete(post)
	db.session.commit()

	flash('Post deleted.', 'success')

	return redirect(url_for('main.home'))
