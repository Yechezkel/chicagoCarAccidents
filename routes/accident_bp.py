from datetime import datetime
from flask import Blueprint, jsonify
from data.data_getter import get_accidents_by_zone , get_accidents_by_zone_and_cause, get_accidents_by_zone_and_date, get_injures_by_zone
from data.data_loader import drop_accidents_collection, load_all_data_from_csv_to_db, create_indexes_accidents_collection

accident_bp =Blueprint('accident_bp', __name__)

@accident_bp.route('/init/', methods=['POST'])
def accident_init():
    drop_accidents_collection()
    load_all_data_from_csv_to_db(r"C:\Users\yechezkel\PycharmProjects\chicagoCarAccidents\csv_files\Traffic_Crashes_800k_rows.csv")
    create_indexes_accidents_collection()
    jsonify({'message': 'finished to load'}), 200


@accident_bp.route('/accidents/<int:zone>/', methods=['GET'])
def route_accidents(zone):
    result = get_accidents_by_zone(zone)
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    message = f"there are {len(result)} accidents in zone {zone}."
    if len(result) == 1:
        message = f"there is {len(result)} accidents in zone {zone}."
    return jsonify(message=message, accidents=result), 200


# to check it here
# @accident_bp.route('/accidents/<int:zone>/<int:year>/<int:month>/<int:day>/', defaults={'radius': 0}, methods=['GET'])

@accident_bp.route('/accidents/<int:zone>/<int:year>/<int:month>/<int:day>/<int:radius>/', methods=['GET'])
def route_accidents_by_date(zone, year, month, day, radius=0):
    date= datetime(year, month, day)
    result = get_accidents_by_zone_and_date(zone, date, radius)
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    message = f"there are {len(result)} accidents in zone {zone} at this date."
    if len(result) == 1:
        message = f"there is {len(result)} accidents in zone {zone} at this date."
    return jsonify(message=message, accidents=result), 200



@accident_bp.route('/accident_causes/<int:zone>/', methods=['GET'])
def route_accidents_causes_by_zone(zone):
    result = get_accidents_by_zone_and_cause(zone)
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    return jsonify(result), 200



@accident_bp.route('/accident_injuries/<int:zone>/', methods=['GET'])
def route_injuries_accidents(zone):
    result = get_injures_by_zone(zone)
    if len(result) == 0:
        return jsonify({'message': 'no accidents found'}), 200
    return jsonify(result), 200


