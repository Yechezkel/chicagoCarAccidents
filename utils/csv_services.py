from csv import DictReader

def read_csv_into_list(csv_path):
    data_list = []
    with open(csv_path, 'r') as file:
        reader = DictReader(file)
        for row in reader:
            data_list.append(dict(row))
    return data_list
