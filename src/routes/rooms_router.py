from typing import Dict, List, Optional
from uuid import UUID

from flask import Blueprint, escape, redirect, request, url_for

from controller.rooms_controller import (
    create_new_room,
    return_all_available_rooms_and_price_range,
    return_all_rooms,
    return_available_rooms_by_type_and_price_range,
    show_room_by_id,
)
from database.connection import db
from schemas.Room import Room, RoomStatus, RoomType

room_endpoint = Blueprint('rooms', __name__)


room_endpoint.route('/room/<uuid:id>/', methods=['GET'])(show_room_by_id)


room_endpoint.route('/room/', methods=['GET'])(return_all_rooms)


room_endpoint.route('/room/', methods=['POST'])(create_new_room)


room_endpoint.route('/room/available/', methods=['GET'])(
    return_all_available_rooms_and_price_range
)


room_endpoint.route('/room/available/<string:room_type>/', methods=['GET'])(
    return_available_rooms_by_type_and_price_range
)
