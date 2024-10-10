from data.data_connect import get_db
from utils.csv_services import read_csv_into_list

def load_from_dict_to_db(document_dict):
    with get_db() as db:
        try:
            injuries = {
                'MOST_SEVERE_INJURY': document_dict['MOST_SEVERE_INJURY'],
                'INJURIES_TOTAL': document_dict['INJURIES_TOTAL'],
                'INJURIES_FATAL': document_dict['INJURIES_FATAL'],
                'INJURIES_INCAPACITATING': document_dict['INJURIES_INCAPACITATING'],
                'INJURIES_NON_INCAPACITATING': document_dict['INJURIES_NON_INCAPACITATING'],
                'INJURIES_REPORTED_NOT_EVIDENT': document_dict['INJURIES_REPORTED_NOT_EVIDENT'],
                'INJURIES_NO_INDICATION': document_dict['INJURIES_NO_INDICATION'],
                'INJURIES_UNKNOWN': document_dict['INJURIES_UNKNOWN']
            }
            date = {
                'CRASH_DATE': document_dict['CRASH_DATE'],
                'CRASH_DATE_EST_I': document_dict['CRASH_DATE_EST_I'],
                'CRASH_DAY_OF_WEEK': document_dict['CRASH_DAY_OF_WEEK'],
                'CRASH_HOUR': document_dict['CRASH_HOUR']
            }
            reason = {
                'PRIM_CONTRIBUTORY_CAUSE': document_dict['PRIM_CONTRIBUTORY_CAUSE'],
                'SEC_CONTRIBUTORY_CAUSE': document_dict['SEC_CONTRIBUTORY_CAUSE']
            }
            accidents = {
                'CRASH_RECORD_ID': document_dict['CRASH_RECORD_ID'],
                'BEAT_OF_OCCURRENCE': document_dict['BEAT_OF_OCCURRENCE'],
                'injuries': injuries,
                'date': date,
                'reason': reason
            }
            db['accidents'].insert_one(accidents)
        except Exception as e:
            print(f"an error occurred, \t CRASH_RECORD_ID: {document_dict["CRASH_RECORD_ID"]} \t error: {e}")


def load_from_csv_to_db(csv_file):
    list_of_dicts = read_csv_into_list(csv_file)
    for document_dict in list_of_dicts:
        load_from_dict_to_db(document_dict)
