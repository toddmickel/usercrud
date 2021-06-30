from flask import Flask, request
from app.database import scan, insert, deactivate_user, fetch_user, upd_user, activate_usr

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
    return out, 201

@app.route("/users/del/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    deactivate_user(uid)
    return out, 200

@app.route("/users/activate/<int:uid>", methods=["PATCH"])
def activate_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    activate_usr(uid)
    return out, 200

    # Create read a single user and update single user end points. And activate user?
@app.route("/users/<int:uid>", methods=["GET"])
def get_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    out["body"] = fetch_user(uid)
    return out, 200

@app.route("/users/update/<int:uid>", methods=["PATCH"])
def update_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    user_data = request.json
    upd_user(
        uid,
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
    )
    return out, 201