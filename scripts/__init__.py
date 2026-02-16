import os
from getpass import getpass
from . import db, crypto

def register():
    username = input("Choose a username: ")
    password = getpass("Choose a password: ")
    salt = os.urandom(16)
    password_hash = crypto.hash_password(password)

    conn = db.get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                    (username, password_hash, salt))
        conn.commit()
        print(f"User '{username}' registered successfully!")
    except:
        print("Username already exists!")
    finally:
        conn.close()

def login():
    username = input("Username: ")
    password = getpass("Password: ")

    conn = db.get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, password_hash, salt FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    conn.close()

    if not row:
        print("User not found!")
        return None, None

    user_id, password_hash, salt = row
    if crypto.check_password(password, password_hash):
        key = crypto.derive_key(password, salt)
        return user_id, key
    else:
        print("Incorrect password!")
        return None, None
