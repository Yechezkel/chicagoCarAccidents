from data.data_loader import get_db

def get_accidents_by_zone(zone: str):
    with get_db() as db:
        result = list(db['accidents'].find({"BEAT_OF_OCCURRENCE" : zone}))
        for item in result:
            item.pop('_id', None)
        return result

