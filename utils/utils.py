from datetime import datetime

def get_date_by_string(string:str): # assuming
    if len(string) > 20:
        return datetime.strptime(string, "%m/%d/%Y %I:%M:%S %p")
    return datetime.strptime(string, "%m/%d/%Y %H:%M")