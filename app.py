from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="tier_db",
        database="mydb",
        user="postgres",
        password="root"  # أو الباسورد اللي حضرتك حطيته
    )
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, email FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    users_list = [{'id': u[0], 'name': u[1], 'email': u[2]} for u in users]
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
