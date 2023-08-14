from flask import Blueprint

from controller.customer_auth_controller import (
    authenticate_user,
    create_new_customer,
)

customer_auth_endpoint = Blueprint('auth', __name__)

customer_auth_endpoint.route('/register/', methods=['POST'])(
    create_new_customer
)
customer_auth_endpoint.route('/login/', methods=['POST'])(authenticate_user)
