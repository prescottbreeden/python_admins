from app import app
from flask import render_template, redirect
from app.models.UserAPI import UserAPI
from flask_bcrypt import Bcrypt

# global variables
bcrypt = Bcrypt(app)
user_api = UserAPI()


class APIControllers:
    def get_all(self):
        users = user_api.get_all()
        return render_template('users.html', users=users)

    def delete(self, id):
        user_api.delete_one(id)
        return redirect('/')
