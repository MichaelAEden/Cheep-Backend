import os

from flask import Flask, send_from_directory

from route.grocery import grocery_blueprint
from route.user import user_blueprint
from route.grocery_list import grocery_list_blueprint
from route.grocery_list_item import grocery_list_item_blueprint


app = Flask(__name__, static_folder=os.environ['REACT_APP_BUILD'])

# Register API routes
app.register_blueprint(grocery_blueprint, url_prefix="/api/grocery")
app.register_blueprint(user_blueprint, url_prefix="/api/user")
app.register_blueprint(grocery_list_blueprint, url_prefix="/api/grocery_list")
app.register_blueprint(grocery_list_item_blueprint, url_prefix="/api/grocery_list_item")

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()
