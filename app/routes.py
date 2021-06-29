from flask import Flask, request
from app.database import scan, insert

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success"
        }
    out["body"] = scan()
    return out

@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "ok": True,
        "message": "Success"
    }
    user_data = request.json
    out["last_row_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        user_data.get("active"),
    )
    return out