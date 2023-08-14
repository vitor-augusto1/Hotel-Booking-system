from functools import wraps
from flask import request
import jwt
from schemas.Token import TokenPayload
from schemas.Customer import Customer
from database.connection import db


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {"error": "Unauthorized"}, 401
        try:
            data: TokenPayload = jwt.decode(token, "my_secret_here", algorithms=["HS256"])
            customer: Customer = db.find_customer_by_id(data['customer_id'])
            print(f"Customer: {customer}")
            if customer is None:
                return {"error": "Invalid authentication token"}, 401
        except Exception as e:
            return {"error": f"Something went wrong: {e}"}, 500
        return func(*args, **kwargs)
    return decorated


