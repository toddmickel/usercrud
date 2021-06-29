
from flask import g
import sqlite3

DATABASE = "user.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out =[]
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["first_name"] = result[1]
        res_dict["last_name"] = result[2]
        res_dict["hobbies"] = result[3]
        res_dict["active"] = result[4]
        out.append(res_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(first_name, last_name, hobbies=None, active=None):
    value_tuple = (first_name, last_name, hobbies, active)
    query = """
        INSERT INTO user(
            first_name,
            last_name,
            hobbies,
            active
        ) VALUES (?, ?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id


def deactivate_user(uid):
    cursor = get_db()
    cursor.execute("UPDATE user SET active=0 WHERE id=?", (uid,))
    cursor.commit()
    cursor.close()