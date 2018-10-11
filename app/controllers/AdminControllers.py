from app import app
from flask import render_template, redirect, session
from app.models.User import User
from app.models.UserAPI import UserAPI
from app.models.NewUser import NewUser
from app.database import connectToMySQL
from flask_bcrypt import Bcrypt

# global variables
bcrypt = Bcrypt(app)
user_api = UserAPI()


class AdminControllers:
    def home(self):
        form = {
            "first_name": '',
            "last_name": '',
            "email": ''
        }
        if 'user_id' not in session:
            all_users = {}
        else:
            all_users = user_api.get_all()
        return render_template('index.html',
                               users=all_users,
                               form=form)

    def register(self, form):
        new_user = NewUser(form)
        session['reg_errors'] = new_user.errors
        if not new_user.errors:
            session['user_id'] = new_user.id
            return redirect('/')
        return render_template('index.html', form=form)

    def login(self, form):
        user = User(form)
        session['login_errors'] = user.errors
        if not user.errors:
            return redirect('/')
        return render_template('index.html',
                               users=0,
                               form=form)

    def logout(self):
        session.pop('user_id', None)
        return redirect('/')

    def make_admin(self, id):
        mysql = connectToMySQL('flask_users')
        query = ("UPDATE users SET status='Administrator'"
                 "WHERE user_id={}".format(id))
        mysql.query_db(query)
        return redirect('/')

    def remove_admin(self, id):
        mysql = connectToMySQL('flask_users')
        query = ("UPDATE users SET status='Normal User'"
                 "WHERE user_id={}".format(id))
        mysql.query_db(query)
        return redirect('/')

    def delete(self, id):
        user_api.delete_one(id)
        return redirect('/')
