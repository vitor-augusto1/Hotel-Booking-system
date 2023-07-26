from flask import Flask
from routes.rooms_router import room_endpoint
from routes.customer_auth_router import customer_auth_endpoint

app: Flask = Flask(__name__)
app.register_blueprint(room_endpoint)
app.register_blueprint(customer_auth_endpoint)


@app.route("/")
def index():
    return {"hello": "World"}
