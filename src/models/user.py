from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase,))

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<User(id='%d', name='%s')>" % (self.user_id, self.name)

    @classmethod
    def from_json(cls, json):
        return cls(name=json['name'])