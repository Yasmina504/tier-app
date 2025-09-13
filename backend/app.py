from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="db",          # اسم السيرفس في docker-compose
        user="root",
        password="root",
        database="mydb"
    )
    return conn

@app.route("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/")
def home():
    return "Backend is working with MySQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

