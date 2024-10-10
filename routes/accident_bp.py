from flask import Blueprint, jsonify


from data.data_getter import get_accidents_by_zone
accident_bp =Blueprint('accident_bp', __name__)

@accident_bp.route('/<int:zone>/', methods=['GET'])
def route_accidents_by_zone(zone):
    result = get_accidents_by_zone(str(zone))
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    message = f"there are {len(result)} accidents in zone {zone}."
    if len(result) == 1:
        message = f"there is {len(result)} accidents in zone {zone}."
    return jsonify(message=message, accidents=result), 200




# @accident_bp.route('/', methods=['GET'])
# def route_accidents():
#     return "gfhbtshts"
