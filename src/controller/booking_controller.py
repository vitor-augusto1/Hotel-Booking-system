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
    token = request.headers["Authorization"].split(" ")[1]
    data: TokenPayload = jwt.decode(token, "my_secret_here", algorithms=["HS256"])
    start_date = request_json['start_date']
    end_date = request_json['end_date']
    rooms_id: List[UUID] = request_json['room_id']
    if None in (start_date, end_date, rooms_id):
        return {"error": "Invalid request."}, 400 
    for id in rooms_id:
        print(f"ID:  {id}")
        room: Room = db.return_room_by_id(id)
        room_status: RoomStatus = room[0][1]
        if room_status == 1:
            return {"forbidden": f"Room '{id}' is already in use."}, 401
    booking: Booking = Booking(
        rooms=rooms_id,
        customer_id=data['customer_id'],
        start_date=start_date,
        end_date=end_date
    )
