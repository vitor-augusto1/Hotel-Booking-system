from typing import List, Optional

from flask import request

from database.connection import db
from decorators.auth_decorator import admin_only
from schemas.Booking import Booking
from schemas.Customer import Customer


@admin_only
def return_all_customers():
    customers: Optional[List[Customer]] = db.return_all_customers()
    return {'customers': customers}, 200


@admin_only
def return_all_bookings():
    bookings: Optional[List[Booking]] = db.return_all_bookings()
    return {'bookings': bookings}, 200
