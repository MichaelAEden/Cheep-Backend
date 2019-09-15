from flask import Flask, Blueprint, request, render_template, send_from_directory

from db.session import Session
from models.user import User
from models.grocery_list import GroceryList
from models.grocery_list_item import GroceryListItem

# Number of images which are displayed in the list preview.
SAMPLE_IMAGES = 5

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


@user_blueprint.route('/<user_id>/list', methods=['GET', 'POST', 'DELETE'])
def user_lists(user_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(GroceryList).filter_by(user_id=user_id).all()
		response = []
		for grocery_list in result:
			json = grocery_list.__json__()
			grocery_list_items_preview = (session
				.query(GroceryListItem)
				.order_by(GroceryListItem.grocery_list_item_id)
				[:SAMPLE_IMAGES]
			)
			json['grocery_list_items_preview'] = grocery_list_items_preview
			response.append(json)
		return { 'grocery_lists': response }
	elif request.method == 'POST':
		grocery_list = GroceryList(user_id=user_id, name=request.json['name'])
		session = Session()
		session.add(grocery_list)
		session.commit()
		return grocery_list.__json__()
	elif request.method == 'DELETE':
		grocery_list = GroceryList(user_id=user_id, name=request.json['name'])
		session = Session()
		session.delete(grocery_list)
		session.commit()
		return grocery_list.__json__()


# Note inclusion of user_id, although list_id is enough to identify the list.
@user_blueprint.route('/<user_id>/list/<list_id>', methods=['GET', 'POST'])
def user_list(user_id, list_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(GroceryListItem).filter_by(grocery_list_id=list_id).all()
	elif request.method == 'POST':
		grocery_list_item = GroceryListItem.from_json(grocery_list_id=list_id, grocery_id=request.json)
		session = Session()
		session.add(grocery_list_item)
		session.commit()
		return grocery_list_item.__json__()
