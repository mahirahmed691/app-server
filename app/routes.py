from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flaskext.mysql import MySQL
from flask_login import current_user, login_user, logout_user, login_required

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'Bucketlist'
app.config['MYSQL_DATABASE_HOST'] = '35.197.193.248'
mysql.init_app(app)
cursor = mysql.connect().cursor()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    username = form.username.data
    password = form.password.data
    remember_me = form.remember_me.data

    if form.validate_on_submit():
	cursor.execute("SELECT * from tbl_user where user_username='" + username + "' and user_password='" + password + "'")
	data = cursor.fetchone()
    	if data is None:
     	    flash('Username or or password is wrong')	
	    return redirect(url_for('login'))
        else:
	    login_user(username, remember=remember_me)
            flash('Login Successful!')
            return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index'))
