from re import escape
from typing import Dict, List, Optional
from uuid import UUID
from schemas.Room import Room, RoomType, RoomStatus
from database.connection import db
from flask import Blueprint, redirect, request, escape, url_for


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


@room_endpoint.route('/room/available/', methods=['GET'])
def return_all_available_rooms_and_price_range():
    args = request.args
    min_price = args.get('min_price')
    max_price = args.get('max_price')
    if None not in (min_price, max_price):
        rooms: Optional[List[Room]] = db.return_all_available_rooms_by_price_range(
            min_price, max_price
        )
    else:
        rooms: Optional[List[Room]] = db.return_all_available_rooms()
    return {"success": {"rooms": rooms}}


@room_endpoint.route('/room/available/<string:room_type>/', methods=['GET'])
def return_available_rooms_by_type_and_price_range(room_type: RoomType):
    args = request.args
    min_price = args.get('min_price')
    max_price = args.get('max_price')
    if None not in (min_price, max_price):
        rooms: Optional[List[Room]] = db.return_available_rooms_by_price_range_and_type(
            min_price, max_price, RoomType[room_type.upper()].name
        )
    else:
        rooms: Optional[List[Room]] = db.return_all_available_rooms_by_its_type(
                    RoomType[room_type.upper()].name
                )
    return {"success": {"rooms": rooms}}


