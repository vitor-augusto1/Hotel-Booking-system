from flask import Flask
from routes.user_auth_router import user_auth_endpoint
from routes.rooms_router import room_endpoint

app: Flask = Flask(__name__)
app.register_blueprint(user_auth_endpoint)
app.register_blueprint(room_endpoint)


@app.route("/")
def index():
    return {"hello": "World"}
