from flask_restful import Resource
from models.car_model import CarModel
from flask import request
import json

class Car(Resource):
    def get(self, id=None):
        if id:
            car = CarModel.find_car_by_id(id)
            if car:
                return {'car': car.to_json()},200
        else:
            cars = CarModel.query.all()
            return {'cars': [car.to_json() for car in cars]},200


    def post(self):
        params = json.loads(request.data)
        make= params.get('make')
        model= params.get('model')
        registration = params.get('registration')
        print(params)

        car = CarModel(make,model,registration)

        car.save_to_db()
        return {'car': car.to_json()}, 200
            
