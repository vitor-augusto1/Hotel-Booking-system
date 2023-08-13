from typing import List, Optional
from flask import request
from database.connection import db
from schemas.Customer import Customer
from schemas.Booking import Booking


def return_all_customers():
    customers: Optional[List[Customer]] = db.return_all_customers()
    return {"customers": customers}, 200


