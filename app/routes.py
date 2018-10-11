from app import app
from app.controllers.APIControllers import APIControllers
from app.controllers.AdminControllers import AdminControllers
from flask import request
app.secret_key = 'WhatIsTheAverageAirSpeedVelocityOfAnUnlaidenSwallow'
api_controllers = APIControllers()
admin_controllers = AdminControllers()


# Admin Controllers
@app.route('/')
def home():
    return admin_controllers.home()


@app.route('/register', methods=['POST'])
def register():
    return admin_controllers.register(request.form)


@app.route('/login', methods=['POST'])
def login():
    return admin_controllers.login(request.form)


@app.route('/logout')
def logout():
    return admin_controllers.logout()


@app.route('/makeadmin/<id>')
def make_admin(id):
    return admin_controllers.make_admin(id)


@app.route('/removeadmin/<id>')
def remove_admin(id):
    return admin_controllers.remove_admin(id)


# API Controllers
@app.route('/users')
def get_all():
    return api_controllers.get_all()


@app.route('/users/<id>')
def get_one(id):
    return api_controllers.get_one()


@app.route('/users/delete/<id>')
def add_friend(id):
    return api_controllers.delete(id)
