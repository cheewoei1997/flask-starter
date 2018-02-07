from flask import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm
from database import db_session
from models import User, Post
from config import Config
from models import LoginForm


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def get_all_users():

    all_users = User.query.all()
    all_posts = Post.query.all()

    context = {
    'all_users': all_users,
    'all_posts': all_posts,
    }
    return render_template('all_users.html', context = context)

@app.route('/form', methods = ['POST', 'GET'])
def form():
    print(request.method)
    if request.method == 'POST':
        result = request.form
        print(result)
    #print(request.form)
    return render_template('form.html')

@app.route('/formresult', methods = ['POST', 'GET'])
def formresult():
    if request.method == 'POST':
        result = request.form  
        context = {

        }
        return render_template('formresult.html', context = context)

@app.route('/user/<name>')
def show_user(name):

    user = User.query.filter(User.name == name).first()

    context = {
    'user': user,
    }
    return render_template('show_user.html', context = context)

@app.route('/new-user/<name>/<email>/<password>')
def create_user(name, email, password):
    new_user = User(name, email, password)
    db_session.add(new_user)
    db_session.commit()

    context = {
        'new_user': new_user,
    }

    return render_template('new_user_created.html', context = context)

@app.route('/triedtologin')
def triedtologin():
    return render_template('triedtologin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/triedtologin')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/post/<post>/<int:fkyou>')
def updates(post, fkyou):
    print(fkyou)
    fkme = int(fkyou)
    new_post = Post(post, fkme)
    db_session.add(new_post)
    db_session.commit()

    context = {
        'new_post': new_post,
    }

    return render_template('new_post_created.html', context = context)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
