import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

def create_table():

    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
        );
    """)

    username1,password1 = "Aritro",hashlib.sha256("Aritro".encode()).hexdigest()
    username2,password2 = "Rupkatha",hashlib.sha256("Rupkatha".encode()).hexdigest()
    username3,password3 = "John",hashlib.sha256("John".encode()).hexdigest()
    username4,password4 = "Doe",hashlib.sha256("Doe".encode()).hexdigest()

    cur.execute(f"INSERT INTO userdata(username,password) VALUES('{username1}','{password1}')")
    cur.execute(f"INSERT INTO userdata(username,password) VALUES('{username2}','{password2}')")
    cur.execute(f"INSERT INTO userdata(username,password) VALUES('{username3}','{password3}')")
    cur.execute(f"INSERT INTO userdata(username,password) VALUES('{username4}','{password4}')")

    conn.commit()

create_table()