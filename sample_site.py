from flask import Flask, render_template, url_for
from markupsafe import escape
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "5352c7c7b5336e0c136ffdd96b00fbad"

posts = [
	{
		'author':'Ajeeth kumar',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted':'April 20, 2018'
	},
	{
		'author':'Shanmuga Valli',
		'title': 'Blog Post 1',
		'content': 'Second post content',
		'date_posted':'April 21, 2018'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/register')
def register():
	form = RegistrationForm
	return render_template('register.html', title="Register", form=form)


@app.route('/login')
def login():
	form = LoginForm
	return render_template('login.html', title="login", form=form)


@app.route('/user/<username>')
def user_name(username):
	return f"Hello {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return f"Your Post ID: {escape(post_id)}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return f"Subpath {escape(subpath)}"

@app.route('/projects/')
def projects():
	return "I am projects"


if __name__ == '__main__':
	app.run(debug=True)