from flask import request
from schemas.Customer import Customer
from utils.encrypt import encrypt_password
from database.connection import db


def create_new_customer():
    args = request.form
    first_name = args.get('firstname')
    print(f"This is the firstname: {first_name}")
    middle_name = args.get('middlename')
    print(f"This is the middlename: {middle_name}")
    last_name = args.get('lastname')
    print(f"This is the lastname: {last_name}")
    password = args.get('password')
    print(f"This is the password: {password}")
    if None in (first_name, last_name, password):
        return {'error': 'There is a missing field'}, 422
    encrypted_password: bytes = encrypt_password(password)
    new_customer: Customer = Customer(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            password=encrypted_password,
            booking_id=None
    )
    #db.create_customers_table()
    db.create_new_customer(new_customer)
    return {
            "success": "Customer created successfully",
           }, 200
