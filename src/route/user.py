from flask import Flask, Blueprint, request, render_template, send_from_directory

from db.session import Session
from models.user import User
from models.grocery_list import GroceryList

user_blueprint = Blueprint("user", __name__)


# TODO: expose this route through UI.
@user_blueprint.route('/', methods=['POST'])
def users():
	if request.method == 'POST':
		user = User.from_json(request.json)
		session = Session()
		session.add(user)
		session.commit()
		return user.__json__()


@user_blueprint.route('/<user_id>/list', methods=['GET', 'POST'])
def user_lists(user_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(GroceryList).filter_by(user_id=user_id).all()
		return { 'grocery_lists': [grocery_list.__json__() for grocery_list in result ] }
	elif request.method == 'POST':
		grocery_list = GroceryList(user_id=user_id, name=request.json['name'])
		session = Session()
		session.add(grocery_list)
		session.commit()
		return grocery_list.__json__()
