from datetime import datetime, timedelta
from flask import jsonify
from data.data_loader import get_db

def get_accidents_by_zone(zone: int):
    with get_db() as db:
        result = list(db['accidents'].find({"BEAT_OF_OCCURRENCE" : zone}))
        for item in result:
            item.pop('_id', None)
        return result




# # it doesn't work I dont know why
# def get_accidents_by_zone_and_date(zone: int, date: datetime, radius: int):
#     date_start = date - timedelta(days=radius)
#     date_end = date + timedelta(days=radius)
#     with get_db() as db:
#         result = list(db['accidents'].find({
#             "BEAT_OF_OCCURRENCE": zone,
#             "date": {
#                 "$gte": date_start,
#                 "$lte": date_end
#             }
#         }))
#         for item in result:
#             item.pop('_id', None)
#         return result


def get_accidents_by_zone_and_date(zone: int, date: datetime, radius: int):
    date_start = date - timedelta(days=radius)
    date_end = date + timedelta(days=radius)
    response = []
    with get_db() as db:
        result = list(db['accidents'].find({"BEAT_OF_OCCURRENCE": zone}))
        for item in result:
            if date_start < item['CRASH_DATE']< date_end:
                item.pop('_id', None)
                response.append(item)
        return response


def get_accidents_by_zone_and_cause(zone: int):
    with get_db() as db:
        pipeline = [
            {"$match": {"BEAT_OF_OCCURRENCE": zone}},
            {
                "$group": {
                    "_id": "$reason.PRIM_CONTRIBUTORY_CAUSE",
                    "total_accidents": {"$sum": 1},
                    "accidents": {"$push": "$$ROOT"}
                }
            },
            {"$project": {"_id": 0, "cause": "$_id", "total_accidents": 1 , "accidents": 1}}
        ]
        result = list(db['accidents'].aggregate(pipeline))
        for item in result:
            for accident in item["accidents"]:
                accident.pop("_id", None)
        new_dict = {i["cause"]: { "total_accidents": i["total_accidents"], "accidents": i["accidents"]  } for i in result}
        return new_dict

# it doesnt work i dont know why
def get_injures_by_zone(zone: int):
    with get_db() as db:
        pipeline = [
            {"$match": { "$and": [ {"BEAT_OF_OCCURRENCE": zone}, { "$expr": { "$gt": [{ "$toInt": "$injuries.INJURIES_TOTAL" }, 0] }} ] }},
            {
                "$group": {
                    "_id": "$BEAT_OF_OCCURRENCE",
                    "caused_death": {"$sum": { "$cond": [{"$gt": [{ "$toInt": "$injuries.INJURIES_FATAL" }, 0]}, 1, 0] }},
                    "not_caused_death": {"$sum": { "$cond": [{"$eq": [{"$ifNull": ["$injuries.INJURIES_FATAL", None]}, None]}, 1, 0] }}
                }
            },
            {"$project": {"_id": 0, "caused_death": 1 , "not_caused_death": 1}}
        ]
        result = list(db['accidents'].aggregate(pipeline))
        return result


# if __name__ == "__main__":
#     print(get_injures_by_zone(225))

