from flask import Blueprint


user_auth_endpoint = Blueprint('user_auth', __name__)


@user_auth_endpoint.route('/user_auth')
def user_auth():
    ...
