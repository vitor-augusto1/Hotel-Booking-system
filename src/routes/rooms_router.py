from re import escape
from uuid import UUID
from schemas.Room import Room, RoomType, RoomStatus
from database.connection import db
from flask import Blueprint, request, escape


room_endpoint = Blueprint('rooms', __name__)




@room_endpoint.route('/room/', methods=['GET'])
def return_all_rooms():
    rooms = db.return_all_rooms()
    return {"rooms": rooms}, 200


