from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",  # Menggunakan penyimpanan memori untuk contoh ini
)


@app.route("/")
@limiter.limit("100 per minute")
def index():
    return "Hello"


@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return jsonify(message="Login successful")


@app.route('/add_data', methods=['POST'])
@limiter.limit("10 per minute")
def add_data():
    try:
        data = request.get_json()

        if data:
            with open('data.txt', 'a') as file:
                file.write(data.get('data', '') + '\n')

            return jsonify(message="Data berhasil ditambahkan ke data.txt"), 201
        else:
            return jsonify(message="Tidak ada data yang diterima"), 400

    except Exception as e:
        return jsonify(message="Terjadi kesalahan: " + str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
