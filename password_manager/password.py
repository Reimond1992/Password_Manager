from getpass import getpass
from . import db, crypto

def add_password(user_id, key, title=None, uname=None, pwd=None):
    if not title:
        title = input("Service name: ")
    if not uname:
        uname = input("Username for service: ")
    if not pwd:
        pwd = getpass("Password for service: ")

    password_enc, nonce = crypto.encrypt(pwd, key)
    conn = db.get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO passwords (user_id, title, username, password_enc, nonce)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, title, uname, password_enc, nonce))
    conn.commit()
    conn.close()
    print(f"Password for '{title}' added!")

def view_passwords(user_id, key):
    conn = db.get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, username, password_enc, nonce FROM passwords WHERE user_id=?", (user_id,))
    rows = cur.fetchall()
    conn.close()

    for r in rows:
        pid, title, uname, p_enc, nonce = r
        try:
            password = crypto.decrypt(p_enc, nonce, key)
        except:
            password = "Decryption error!"
        print(f"[{pid}] {title} | {uname} | {password}")

def delete_password(user_id):
    pid = input("Enter the ID of the password to delete: ")
    conn = db.get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM passwords WHERE id=? AND user_id=?", (pid, user_id))
    conn.commit()
    conn.close()
    print(f"Password ID {pid} deleted!")
