from flask import session
from app import app
from app.database import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    def __init__(self, form):
        self._email = form['login_email'].lower()
        self._password = form['login_password']
        self.errors = {}
        self.validate()

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    def validate(self):
        mysql = connectToMySQL('flask_users')
        query = "SELECT * FROM users where email=%(email)s"
        user = mysql.query_db(query, {"email": self.email})
        print(user)
        if (user):
            db_pw = user[0]['password']
            verified = bcrypt.check_password_hash(db_pw, self.password)
            print(verified)
            if verified:
                session['user_id'] = user[0]['user_id']
            else:
                self.errors['password'] = "Inccorect Password"
        else:
            self.errors['email'] = "Email not found"
        return self
