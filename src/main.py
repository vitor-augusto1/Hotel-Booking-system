from flask import Flask

from routes.admin_router import admin_endpoints
from routes.book_router import book_endpoint
from routes.customer_auth_router import customer_auth_endpoint
from routes.rooms_router import room_endpoint

app: Flask = Flask(__name__)
app.register_blueprint(room_endpoint)
app.register_blueprint(customer_auth_endpoint)
app.register_blueprint(book_endpoint)
app.register_blueprint(admin_endpoints)


@app.route('/')
def index():
    return {'hello': 'World'}
