from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase,))

class Grocery(Base):
    __tablename__ = 'grocery'

    grocery_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    image = Column(String)

    def __repr__(self):
        return "<Grocery(id='%d', name='%s', price='%d', image='%s')>" % (
            self.grocery_id, self.name, self.price, self.image)

    @classmethod
    def from_json(cls, json):
        return cls(name=json['name'], price=json['price'], image=json['image'])
