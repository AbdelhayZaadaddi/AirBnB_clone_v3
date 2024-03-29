#!/usr/bin/python3
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
    alls = {}
    classes = {"Amenity": "amenities",
                "City": "cities",
                "Place": "places",
                "Review": "reviews",
                "State": "states",
                "User": "users"}
    for class_ in classes:
        count = storage.count(class_)
        alls[classes.get(class_)] = count
    return jsonify(alls)
