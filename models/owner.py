from db import db

class OwnerModel(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False, unique= True)

    #cars= db.relationship('CarModel', lazy='dynamic')

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def find_owner_by_id(cls,id):
        return cls.query.filter_by(id=id).first()


    def save(self):
        db.session.add(self)
        db.session.commit()


