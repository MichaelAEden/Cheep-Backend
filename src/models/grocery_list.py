from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase,))

class GroceryList(Base):
    __tablename__ = 'grocery_list'

    grocery_list_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)

    def __repr__(self):
        return "<GroceryList(id='%d', user_id='%d', name='%s')>" % (
        	self.grocery_list_id, self.user_id, self .name)

    @classmethod
    def from_json(cls, json):
        return cls(user_id=json['user_id'], name=json['name'])
