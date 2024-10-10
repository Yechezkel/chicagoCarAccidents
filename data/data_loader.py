from data.data_connect import get_db
from utils.csv_services import read_csv_into_list
from utils.utils import get_date_by_string

def drop_accidents_collection():
    with get_db() as db:
        db['accidents'].drop()

def load_from_dict_to_db(document_dict, db):
    try:
        injuries_keys = ['INJURIES_TOTAL', 'INJURIES_FATAL','INJURIES_INCAPACITATING', 'INJURIES_NON_INCAPACITATING', 'INJURIES_REPORTED_NOT_EVIDENT', 'INJURIES_NO_INDICATION','INJURIES_UNKNOWN']
        injuries = {key: int(document_dict[key]) for key in injuries_keys if document_dict[key] not in [None, "", "0"]}
        injuries["MOST_SEVERE_INJURY"] = document_dict["MOST_SEVERE_INJURY"]
        cause = {
            'PRIM_CONTRIBUTORY_CAUSE': document_dict['PRIM_CONTRIBUTORY_CAUSE'],
            'SEC_CONTRIBUTORY_CAUSE': document_dict['SEC_CONTRIBUTORY_CAUSE']
        }
        accident = {
            'CRASH_RECORD_ID': document_dict['CRASH_RECORD_ID'],
            'BEAT_OF_OCCURRENCE': 0 if len(document_dict['BEAT_OF_OCCURRENCE'])== 0 else int(document_dict['BEAT_OF_OCCURRENCE']),
            'CRASH_DATE': get_date_by_string(document_dict["CRASH_DATE"]),
            'injuries': injuries,
            'cause': cause
        }
        db['accidents'].insert_one(accident)
    except Exception as e:
        print(f"an error occurred, \t CRASH_RECORD_ID: {document_dict["CRASH_RECORD_ID"]} \t error: {e}")


def load_from_csv_to_db(csv_file):
    list_of_dicts = read_csv_into_list(csv_file)
    with get_db() as db:
        for document_dict in list_of_dicts:
            load_from_dict_to_db(document_dict,db)




































# if __name__ == '__main__':
#     # def check():
# #         list_of_dicts = read_csv_into_list(r"C:\Users\yechezkel\PycharmProjects\chicagoCarAccidents\csv_files\Traffic_Crashes_20k_rows.csv")
# #         count = 0
# #         for document_dict in list_of_dicts:
# #             # if document_dict['CRASH_DATE'] == "" or document_dict['CRASH_DATE'] is None:
# #
# #             if document_dict['CRASH_DATE_EST_I'].strip() == "" :
# #                 # print(f"{count} both")
# #                 count += 1
# #                 print(f"{count}  len: {len(document_dict['CRASH_DATE_EST_I'])}  content: {document_dict['CRASH_DATE_EST_I']}   {type(document_dict['CRASH_DATE_EST_I']) }")
# #
# #
#     def check2():
#         list_of_dicts = read_csv_into_list(
#             r"C:\Users\yechezkel\PycharmProjects\chicagoCarAccidents\csv_files\Traffic_Crashes_20k_rows.csv")
#         count = 0
#         for document_dict in list_of_dicts:
#
#             if document_dict["CRASH_RECORD_ID"] in[ "012d8a63ccf362651e5bc25cafbabad97ea7a08cfe827de2807a00c77ac0e383b1e062feea4883d6e9c4bb2a47e044bf7212fa93aa5aae6118565f6b25e42b3f" \
#                     , "1f5b660acb4d882bb388139187d8bd9b0245a8aa91388af94c3a223596808666f74251fbf0c09542b320d649f5b7a56c05fbd06d6db147a7611397d93104c240"] :
#                 count += 1
#                 # print(count,"""   """,document_dict['BEAT_OF_OCCURRENCE'],  )
#                 print(f"{count}  len: {len(document_dict['BEAT_OF_OCCURRENCE'])}  content: '{len(document_dict['BEAT_OF_OCCURRENCE'])}'   {len(document_dict['BEAT_OF_OCCURRENCE'])}")
#
#     print(int('0'))
#     check2()
