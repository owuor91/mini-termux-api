from flask import Flask,request
from flask_restful import Api
from db import db
from resources.car import Car
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"pwd": "home",
            "asserts": 5,
            "wantie": True}, 200


@app.route('/greetings')
def greet():
    name = request.args.get('name')
    return {'status': 'OK',
            'resp': 'Hello %s'%(name)},200

api.add_resource(Car, '/cars', '/cars/<int:id>')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
