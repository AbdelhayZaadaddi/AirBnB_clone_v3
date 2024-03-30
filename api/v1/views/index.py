#!/usr/bin/python3
"""the index module for the views package"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def get_status():
    """ Returns the status of the API """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def count():
    """ Returns the count of all classes """
    return jsonfy({"amenity": storage.count("Amenities"),
                "city": storage.count("Cities"),
                "place": storage.count("Places"),
                "review": storage.count("Reviews"),
                "state": storage.count("States"),
                "user": storage.count("Users")}
