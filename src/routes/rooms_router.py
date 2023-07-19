from re import escape
from uuid import UUID
from schemas.Room import Room, RoomType, RoomStatus
from database.connection import db
from flask import Blueprint, request, escape


room_endpoint = Blueprint('rooms', __name__)


@room_endpoint.route('/room/<uuid:id>/', methods=['GET'])
def show_room_by_id(id: UUID):
    room: Room = db.return_room_by_id(id)
    return {"room": room}, 200


@room_endpoint.route('/room/', methods=['GET'])
def return_all_rooms():
    rooms = db.return_all_rooms()
    return {"rooms": rooms}, 200


@room_endpoint.route('/room/', methods=['POST'])
def create_new_room():
    room_type = request.form['room_type']
    room_price = request.form['room_price']
    new_room: Room = Room(
        room_status=RoomStatus.EMPTY,
        room_type=RoomType(int(room_type)),
        price=room_price
    )
    db.create_new_room(new_room)
    return {"success": {"room": f"{new_room.id}"}}, 200
