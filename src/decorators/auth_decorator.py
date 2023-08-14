from functools import wraps

import jwt
from flask import request

from database.connection import db
from schemas.Customer import Customer
from schemas.Token import TokenPayload


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return {'error': 'Unauthorized'}, 401
        try:
            data: TokenPayload = jwt.decode(
                token, 'my_secret_here', algorithms=['HS256']
            )
            customer: Customer = db.find_customer_by_id(data['customer_id'])
            print(f'Customer: {customer}')
            if customer is None:
                return {'error': 'Invalid authentication token'}, 401
        except Exception as e:
            return {'error': f'Something went wrong: {e}'}, 500
        return func(*args, **kwargs)

    return decorated


def admin_only(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return {'error': 'Unauthorized'}, 401
        try:
            data: TokenPayload = jwt.decode(
                token, 'my_secret_here', algorithms=['HS256']
            )
            customer: Customer = db.find_customer_by_id(data['customer_id'])
            print(f'Customer: {customer}')
            if customer is None:
                return {'error': 'Invalid authentication token'}, 401
            is_customer_not_admin: bool = not data['is_admin']
            if is_customer_not_admin:
                return {'error': 'Unauthorized'}, 403
        except Exception as e:
            return {'error': f'Something went wrong: {e}'}, 500
        return func(*args, **kwargs)

    return decorated
