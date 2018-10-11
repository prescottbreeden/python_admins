from app import app
from app.controllers import Controllers
from flask import request
app.secret_key = 'WhatIsTheAverageAirSpeedVelocityOfAnUnlaidenSwallow'
controllers = Controllers()


@app.route('/')
def home():
    return controllers.home()


@app.route('/register', methods=['POST'])
def register():
    return controllers.register(request.form)


@app.route('/login', methods=['POST'])
def login():
    return controllers.login(request.form)


@app.route('/logout')
def logout():
    return controllers.logout()


@app.route('/delete/<id>')
def add_friend(id):
    return controllers.delete(id)


@app.route('/makeadmin/<id>')
def make_admin(id):
    return controllers.make_admin(id)


@app.route('/removeadmin/<id>')
def remove_admin(id):
    return controllers.remove_admin(id)
