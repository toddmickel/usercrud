import requests

TEST_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Skiing",
    "active": 1
}

UPDATED_USER = {
    "last_name": "Mickel",
}

def test_user_creation():
    out = requests.post("http://127.0.0.1:5000/users", json=TEST_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print("Something went wrong.")

def test_user_deactivate():
    out = requests.delete("http://127.0.0.1:5000/users/del/2")
    if out.status_code == 200:
        print(out.json())
    else:
        print(out)
        print("Something is wrong with delete.")

def test_user_activate():
    out = requests.patch("http://127.0.0.1:5000/users/activate/2")
    if out.status_code == 200: print(out.json())
    else: print("Something is wrong with activate.")

def test_user_update():
    out = requests.patch("http://127.0.0.1:5000/users/update/2", json=UPDATED_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print(out)
        print("Something is wrong with update.")

if __name__ == "__main__":
    #test_user_creation()
    #test_user_deactivate()
    test_user_activate()
    #test_user_update()