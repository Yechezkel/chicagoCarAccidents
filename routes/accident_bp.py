from flask import Blueprint, jsonify
from data.data_getter import get_accidents_by_zone
accident_bp =Blueprint('accident_bp', __name__)

@accident_bp.route('/<int:zone>/', methods=['GET'])
def route_accidents_by_zone(zone):
    result = get_accidents_by_zone(str(zone))
    return jsonify(result),200

@accident_bp.route('/', methods=['GET'])
def route_accidents():
    return "gfhbtshts"
