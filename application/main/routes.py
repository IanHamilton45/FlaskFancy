from flask import render_template, request, Blueprint
from application.models import Posts

main = Blueprint('main', __name__)

NUM_POSTS_PER_PAGE = 4

@main.route('/')
@main.route('/home')
def home():
	page = request.args.get('page', 1, type=int)
	postData = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=NUM_POSTS_PER_PAGE)

	return render_template('home.html', posts=postData)

@main.route('/about')
def about():
	return render_template('about.html', title='About')
