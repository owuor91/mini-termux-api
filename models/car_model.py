from db import db

class CarModel(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    registration = db.Column(db.String(16))
    #owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    #owner = db.relationship('OwnerModel')


    def __init__(self, make, model, registration):
        self.make = make
        self.model = model
        self.registration = registration
        #self.owner_id = owner_id


    @classmethod
    def find_car_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def to_json(self):
        return {'id': self.id,
                'make': self.make,
                'model': self.model,
                'registration': self.registration}
                #'owner_id': self.owner_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

