from app import app
from app.database import connectToMySQL
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class NewUser:
    def __init__(self, info):
        self._first_name = info['first_name'].capitalize()
        self._last_name = info['last_name'].capitalize()
        self._email = info['email'].lower()
        self._password = info['password']
        self._confirm_pw = info['password2']
        self.errors = {}
        self.validate()

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def confirm_pw(self):
        return self._confirm_pw

    def validate(self):

        # first name
        if len(self.first_name) < 3:
            self.errors['first_name'] = "First name must be 3+ characters"

        # last name
        if len(self.last_name) < 3:
            self.errors['last_name'] = "Last name must be 3+ characters"

        # email
        if not re.match(EMAIL_REGEX, self.email):
            self.errors['email'] = "Email must be a valid email"

        # password
        if len(self.password) < 6:
            self.errors['password'] = "Password must be 6+ characters"
        if self.password != self.confirm_pw:
            self.errors['password'] = "Passwords do not match"

        if not self.errors:
            self.add_user()

    def add_user(self):
        pw = self.password
        pw = bcrypt.generate_password_hash(pw)
        mysql = connectToMySQL('flask_users')
        query = '''
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (
            %(first_name)s, %(last_name)s, %(email)s, %(password)s );
        '''
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": pw
        }
        self.id = mysql.query_db(query, data)
        return self
