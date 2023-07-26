from typing import Dict, List, Optional
from uuid import UUID
from schemas.Room import Room, RoomType, RoomStatus
from database.connection import db
from flask import Blueprint, redirect, request, escape, url_for
from controller.rooms_controller import show_room_by_id, return_all_rooms, create_new_room, return_all_available_rooms_and_price_range, return_available_rooms_by_type_and_price_range


room_endpoint = Blueprint('rooms', __name__)


room_endpoint.route('/room/<uuid:id>/', methods=['GET'])(show_room_by_id)


room_endpoint.route('/room/', methods=['GET'])(return_all_rooms)


room_endpoint.route('/room/', methods=['POST'])(create_new_room)


room_endpoint.route('/room/available/', methods=['GET'])(return_all_available_rooms_and_price_range)


room_endpoint.route('/room/available/<string:room_type>/', methods=['GET'])(return_available_rooms_by_type_and_price_range)
