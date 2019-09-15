from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase,))

class GroceryListItem(Base):
    __tablename__ = 'grocery_list_item'

    grocery_list_item_id = Column(Integer, primary_key=True)
    grocery_list_id = Column(Integer) #, primary_key=True)
    grocery_id = Column(Integer)

    def __repr__(self):
        return "<GroceryListItem(id='%d', grocery_list_id='%d', grocery_id='%d')>" % (
        	self.grocery_list_item_id, self.grocery_list_id, self.grocery_id)

    @classmethod
    def from_json(cls, json):
        return cls(
        	grocery_list_id=json['grocery_list_id'],
        	grocery_id=json['grocery_id']
        )
