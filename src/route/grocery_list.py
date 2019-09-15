from flask import Flask, Blueprint, request, render_template, send_from_directory

from db.session import Session
from models.grocery_list import GroceryList

grocery_list_blueprint = Blueprint("grocery_list", __name__)

#Gets grocery_list by id
@grocery_list_blueprint.route('/<grocery_list_id>', methods=['GET'])
def grocery_list(grocery_list_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(GroceryList).filter_by(grocery_list_id=grocery_list_id).first()
		if result is None:
			return ('Grocery list not found.', 404)
		else:
			return result.__json__()

# Not sure if this code makes sense
# @grocery_list_blueprint.route('/<user_id>/list/<grocery_list_id>', methods=['GET'])
# def user_list(user_id, list_id):
# 	if request.method == 'GET':
# 		result = session.query(GroceryList).filter_by(user_id=user_id, grocery_list_id=grocery_list_id).first()
# 		if result is None:
# 			return ('Grocery list not found.', 404)
# 		else:
# 			return result.__json__()
