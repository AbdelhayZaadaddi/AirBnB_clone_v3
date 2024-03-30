#!/usr/bin/python3
"""App views for AirBnB_clone_v3

Indexing app views
"""

from models import storage
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """return status of the API"""
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats')
def count():
    """return count of all classes in storage"""
    return jsonify({"amenity": storage.count("Amenities"),
               "city": storage.count("Cities"),
               "place": storage.count("Places"),
               "review": storage.count("Reviews"),
               "state": storage.count("States"),
               "user": storage.count("Users")})
