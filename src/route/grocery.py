from flask import Flask, Blueprint, request, render_template, send_from_directory

from db.session import Session
from models.grocery import Grocery

grocery_blueprint = Blueprint("grocery", __name__)


@grocery_blueprint.route('/', methods=['GET', 'POST'])
def groceries():
	if request.method == 'POST':
		grocery = Grocery.from_json(request.json)
		session = Session()
		session.add(grocery)
		session.commit()
		return grocery.__json__()
	elif request.method == 'GET':
		session = Session()
		return { 'data': [grocery.__json__() for grocery in session.query(Grocery).all()] }


@grocery_blueprint.route('/<grocery_id>', methods=['GET'])
def grocery(grocery_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(Grocery).filter_by(grocery_id=grocery_id).first()
		if result is None:
			return ('Grocery not found.', 404)
		else:
			return result.__json__()
