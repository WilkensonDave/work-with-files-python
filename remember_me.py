from pathlib import Path
import json


def get_stored_username(path):
        content = path.read_text()
        username = json.loads(content)
        print(f"Welcome to this programme {username}")


def stored_username(path):
    username = input("What is your name?: ")
    content = json.dumps(username)
    path.write_text(content)
    print(f"We will always remember next time you come {username}")


def remember_user():
    path = Path('username.json')

    if path.exists():
        get_stored_username(path)

    else:
        stored_username(path)


remember_user()