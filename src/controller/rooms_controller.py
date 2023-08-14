from flask import request
from database.connection import db
from schemas.Room import Room, RoomType, RoomStatus
from decorators.auth_decorator import login_required, admin_only
from typing import List, Optional
from uuid import UUID


@login_required
def show_room_by_id(id: UUID):
    room: Room = db.return_room_by_id(id)
    return {"room": room}, 200


@login_required
def return_all_rooms():
    rooms = db.return_all_rooms()
    return {"rooms": rooms}, 200


@admin_only
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


@login_required
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


@login_required
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
