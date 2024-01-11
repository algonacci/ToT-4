from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("02_sql_injection/index.html")


@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return render_template('02_sql_injection/index.html', result=result)


if __name__ == '__main__':
    app.run()
