#!/usr/bin/python3
"""App views for AirBnB_clone_v3

Indexing app views
"""

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
    alls = {}
    classes = {"Amenity": "Amenities",
               "City": "Cities",
               "Place": "Places",
               "Review": "Reviews",
               "State": "States",
               "User": "Users"}
    for classx in classes:
        count = storage.count(classx)
        alls[classes.get(classx)] = count
    return jsonify(alls)
