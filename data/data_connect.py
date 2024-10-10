from pymongo import MongoClient
from contextlib import contextmanager

@contextmanager
def get_db():
    client = MongoClient('localhost', 27017)
    db = client['chicagoCarAccidents_1']
    try:
        yield db
    finally:
        client.close()