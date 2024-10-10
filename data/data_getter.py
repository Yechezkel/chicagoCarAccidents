from data.data_loader import get_db
import json

def get_accidents_by_zone(zone: int):
    with get_db() as db:
        result = list(db['accidents'].find({"BEAT_OF_OCCURRENCE" : zone}))
        for item in result:
            item.pop('_id', None)
        return result



def get_accidents_by_zone_and_cause(zone: int):
    with get_db() as db:
        pipeline = [
            {"$match": {"BEAT_OF_OCCURRENCE": zone}},
            {
                "$group": {
                    "_id": "$reason.PRIM_CONTRIBUTORY_CAUSE",
                    "total_accidents": {"$sum": 1},
                    # "accidents": {"$push": "$$ROOT"}
                }
            },
            {"$project": {"_id": 0, "cause": "$_id", "total_accidents": 1}}   # , "accidents": 1}}
        ]
        result = list(db['accidents'].aggregate(pipeline))
        new_dict = {i["cause"]: i["total_accidents"] for i in result}
        # print(json.dumps(new_dict, indent=4))
        return new_dict


def get_injures_by_zone(zone: int):
    with get_db() as db:
        pipeline = [
            {"$match": { "$and": [ {"BEAT_OF_OCCURRENCE": zone}, { "$expr": { "$gt": [{ "$toInt": "$injuries.INJURIES_TOTAL" }, 0] }} ] }},
            {
                "$group": {
                    "_id": "$BEAT_OF_OCCURRENCE",
                    "caused_death": {"$sum": { "$cond": [{"$gt": [{ "$toInt": "$injuries.INJURIES_FATAL" }, 0]}, 1, 0] }},
                    "not_caused_death": {"$sum": { "$cond": [{"$eq": [{ "$toInt": "$injuries.INJURIES_FATAL" }, 0]}, 1, 0] }}
                }
            },
            {"$project": {"_id": 0, "caused_death": 1 }}
        ]
        result = list(db['accidents'].aggregate(pipeline))
        return result


# if __name__ == "__main__":
#     print(get_injures_by_zone(1234))

