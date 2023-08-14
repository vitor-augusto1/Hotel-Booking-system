from typing import Optional
from uuid import UUID
from flask import request
import jwt
from schemas.Customer import Customer
from schemas.Token import TokenPayload
from utils.encrypt import encrypt_password, check_password
from database.connection import db


jwt_secret: str = "my_secret_here"


def create_new_customer():
    args = request.form
    first_name = args.get('firstname')
    middle_name = args.get('middlename')
    last_name = args.get('lastname')
    email = args.get('email')
    password = args.get('password')
    if None in (first_name, last_name, password):
        return {'error': 'There is a missing field'}, 422
    encrypted_password: bytes = encrypt_password(password)
    new_customer: Customer = Customer(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            password=encrypted_password,
            booking_id=None
    )
    # db.create_customers_table()
    db.create_new_customer(new_customer)
    return {
            "success": "Customer created successfully",
           }, 200


def authenticate_user():
    args = request.form
    email = args.get('email')
    password = args.get('password')
    customer: Optional[Customer] = db.find_customer_by_email(email)
    if customer is None:
        return {"user": "Not found"}, 404
    customer_stored_password: str = customer[0][5]
    user_provided_a_valid_password: bool = check_password(
            password, customer_stored_password.encode('utf8')
    )
    if (not user_provided_a_valid_password):
        return {"error": "Invalid Credentials"}, 401
    customer_id: UUID = customer[0][0]
    jwt_payload: TokenPayload = TokenPayload(customer_id=customer_id, is_admin=False)
    token = jwt.encode(jwt_payload.dict(), jwt_secret, algorithm="HS256")
    print(f"Generated token: {token}")
    return {"success": token}, 200
