from flask import Flask, Blueprint, request, render_template, send_from_directory

from db.session import Session
from models.grocery import Grocery

grocery_blueprint = Blueprint("grocery", __name__)

@grocery_blueprint.route('/', methods=['GET', 'POST'])
def groceries():
	if request.method == 'POST': #makes new grocery
		grocery = Grocery.from_json(request.json)
		session = Session()
		session.add(grocery)
		session.commit()
		return grocery.__json__()
	elif request.method == 'GET': #grabs all groceries from SQL database
		session = Session()
		result = session.query(Grocery).order_by(Grocery.grocery_id).all()
		return { 'groceries': [grocery.__json__() for grocery in result ] }

#when you click into a specific grocery, grabs by id
@grocery_blueprint.route('/<grocery_id>', methods=['GET'])
def grocery(grocery_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(Grocery).filter_by(grocery_id=grocery_id).first()
		if result is None:
			return ('Grocery not found.', 404)
		else:
			return result.__json__()

#enables search by grocery name
@grocery_blueprint.route('/search/<grocery_name>', methods=['GET'])
def search(grocery_name):
	if request.method == 'GET':
		session = Session()
		result = session.query(Grocery).filter_by(name=grocery_name).first()
		if result is None:
			return ('Grocery not found.', 404)
		else:
			return result.__json__()
