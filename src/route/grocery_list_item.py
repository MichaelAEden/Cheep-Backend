from flask import Flask, Blueprint, request, render_template, send_from_directory

from db.session import Session
from models.grocery_list_item import GroceryListItem

grocery_list_item_blueprint = Blueprint("grocery_list_item", __name__)

#Makes new grocery_list_item, with grocery_list_id->grocery_id
@grocery_list_item_blueprint.route('/', methods=['POST'])
def grocery_list_items():
	if request.method == 'POST':
		grocery_list_item = GroceryListItem.from_json(request.json)
		session = Session()
		session.add(grocery_list_item)
		session.commit()
		return grocery_list_item.__json__()

#Gets grocery_list_item by id, delete by id
#TODO: might be good to move to user.py
@grocery_list_item_blueprint.route('/<grocery_list_item_id>', methods=['GET', 'DELETE'])
def grocery_list_item(grocery_list_item_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(GroceryListItem).filter_by(grocery_list_item_id=grocery_list_item_id).first()
		if result is None:
			return ('Grocery list item not found.', 404)
		else:
			return result.__json__()
	elif request.method == 'DELETE':
		session = Session()
		grocery_list_item = session.query(GroceryListItem).filter_by(grocery_list_item_id=grocery_list_item_id).first()
		if grocery_list_item is None:
			return ('Grocery list item not found.', 404)
		else:
			session.delete(grocery_list_item)
			session.commit()
			return grocery_list_item.__json__()
