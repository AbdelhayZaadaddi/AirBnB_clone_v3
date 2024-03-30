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
<<<<<<< HEAD
    classes = {"amenity": "Amenities",
               "city": "Cities",
               "place": "Places",
               "review": "Reviews",
               "state": "States",
               "user": "Users"}
=======
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
>>>>>>> parent of 934e7e7... Revert "..."
    for classx in classes:
        count = storage.count(classx)
        alls[classes.get(classx)] = count
    return jsonify(alls)
