from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return {"pwd": "home",
            "asserts": 5,
            "wantie": True}, 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
