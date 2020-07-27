from flask import request
from flask_restful import Resource
from models.owner import OwnerModel
import json

class Owner(Resource):
    def post(self):
        data = json.loads(request.data)
        name = data.get('name')
        phone_number = data.get('phone_number')
        owner= OwnerModel(name, phone_number)
        owner.save()
        return json.dumps(owner),200

    def get(self, id=None):
        if id:
            owner = OwnerModel.find_owner_by_id(id)
            return json.dumps(owner), 200
        else:
            owners= OwnerModel.query.all()
            return {'owners': [json.dumps(o) for o in owners]},200
