from functools import wraps
from flask import request
import jwt
from schemas.Token import TokenPayload
from schemas.Customer import Customer
from database.connection import db
import datetime
import pytz


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
            utc_now = datetime.datetime.utcnow().replace(tzinfo=None)
            brasilia_timezone = pytz.timezone('America/Sao_Paulo')
            utc_now_brasilia_timezone = utc_now.astimezone(brasilia_timezone).replace(tzinfo=None)
            token_expire_date = data["exp"]
            if utc_now_brasilia_timezone > datetime.datetime.fromtimestamp(token_expire_date):
                return {"error": "Expired token"}, 401
        except Exception as e:
            return {"error": f"Something went wrong: {e}"}, 500
        return func(*args, **kwargs)
    return decorated
