from db import db

class CarModel(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    registration = db.Column(db.String(16))


    def __init__(self, make, model, registration):
        self.make = make
        self.model = model
        self.registration = registration


    @classmethod
    def find_car_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def to_json(self):
        return {'id': self.id,
                'make': self.make,
                'model': self.model,
                'registration': self.registration}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

