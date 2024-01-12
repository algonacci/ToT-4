from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins=["https://example.com", "http://127.0.0.1:5500"])


@app.route('/')
def hello_world():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
