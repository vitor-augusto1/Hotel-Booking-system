from typing import List, Optional
from flask import request
from database.connection import db
from schemas.Customer import Customer
from schemas.Booking import Booking


def return_all_customers():
    customers: Optional[List[Customer]] = db.return_all_customers()
    return {"customers": customers}, 200


def return_all_bookings():
    bookings: Optional[List[Booking]] = db.return_all_bookings()
    return {"bookings": bookings}, 200
