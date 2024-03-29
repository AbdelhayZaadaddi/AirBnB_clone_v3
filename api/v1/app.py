#!/usr/bin/python3
"""The main entry point for the ARBNB API"""

from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """Closes the storage"""
    storage.close()


if __name__ == "__main__":
    HBNB_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    HBNB_PORT = getenv("HBNB_API_PORT", 5000)
    app.run(host=HBNB_HOST, port=HBNB_PORT, debug=True, threaded=True)
