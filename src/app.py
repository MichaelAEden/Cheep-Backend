import os

from flask import Flask, request, render_template, send_from_directory

from db.session import Session
from models.grocery import Grocery

app = Flask(__name__, static_folder=os.environ['REACT_APP_BUILD'])


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder + path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/grocery', methods=['GET', 'POST'])
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


@app.route('/api/grocery/<grocery_id>', methods=['GET'])
def grocery(grocery_id):
	if request.method == 'GET':
		session = Session()
		result = session.query(Grocery).filter_by(grocery_id=grocery_id).first()
		if result is None:
			return ('Grocery not found.', 404)
		else:
			return result.__json__()


if __name__ == "__main__":
    app.run()
