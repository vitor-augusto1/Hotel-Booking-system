from typing import List, Optional
from uuid import UUID
from flask import request
from decorators.auth_decorator import login_required
from schemas.Room import Room, RoomStatus
from schemas.Booking import Booking
from schemas.Token import TokenPayload
from database.connection import db
import jwt


@login_required
def book_a_room():
    request_json = request.get_json()
    start_date = request_json['start_date']
    end_date = request_json['end_date']
    rooms_id: List[UUID] = request_json['room_id']
    if None in (start_date, end_date, rooms_id):
        return {"error": "Invalid request."}, 400 
