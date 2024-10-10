from flask import Blueprint, jsonify
from data.data_loader import load_from_csv_to_db


from data.data_getter import get_accidents_by_zone , get_accidents_by_zone_and_cause
accident_bp =Blueprint('accident_bp', __name__)

# @accident_bp.route('/init/', methods=['POST'])
# def accident_init():
#     load_from_csv_to_db(r"C:\Users\yechezkel\PycharmProjects\chicagoCarAccidents\csv_files\Traffic_Crashes_20k_rows.csv")
#     return 200


@accident_bp.route('/accidents/<int:zone>/', methods=['GET'])
def route_accidents_by_zone(zone):
    result = get_accidents_by_zone(zone)
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    message = f"there are {len(result)} accidents in zone {zone}."
    if len(result) == 1:
        message = f"there is {len(result)} accidents in zone {zone}."
    return jsonify(message=message, accidents=result), 200



@accident_bp.route('/accident_causes/<int:zone>/', methods=['GET'])
def route_accidents_by_zone_and_cause(zone):
    result = get_accidents_by_zone_and_cause(str(zone))
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    return jsonify(result), 200



# @accident_bp.route('/', methods=['GET'])
# def route_accidents():
#     return "gfhbtshts"
