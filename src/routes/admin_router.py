from flask import Blueprint

from controller.admin_controller import (
    return_all_bookings,
    return_all_customers,
)

admin_endpoints = Blueprint('admin', __name__)


admin_endpoints.route('/customers/', methods=['GET'])(return_all_customers)
admin_endpoints.route('/bookings/', methods=['GET'])(return_all_bookings)
