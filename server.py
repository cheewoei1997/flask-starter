from flask import Flask, render_template
from database import db_session
from models import User
app = Flask(__name__)

@app.route('/')
def get_all_users():

    all_users = User.query.all()

    context = {
    'all_users': all_users,
    }
    return render_template('all_users.html', context = context)


@app.route('/user/<name>')
def show_user(name):

    user = User.query.filter(User.name == name).first()

    context = {
    'user': user,
    }
    return render_template('show_user.html', context = context)

@app.route('/new-user/<name>/<email>/<password>')
def create_user(name, email,password):
    new_user = User(name, email, password)
    db_session.add(new_user)
    db_session.commit()

    context = {
        'new_user': new_user,
    }

    return render_template('new_user_created.html', context = context)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
