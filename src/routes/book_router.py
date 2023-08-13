from flask import Blueprint
from controller.booking_controller import book_a_room


book_endpoint = Blueprint('booking', __name__)


book_endpoint.route('/booking/', methods=['POST'])(book_a_room)
