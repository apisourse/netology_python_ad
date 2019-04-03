import csv
from pymongo import MongoClient

client = MongoClient()
db = client['concerts_db']


def read_csv(filename):
    pass


def add_artist(artist):
    is_exists = db.artists.find_one({'name': artist})
    if is_exists:
        print(f'{artist} уже существует')
        return is_exists['_id']

    res = db.artist.insert_one({'name': artist})
    print(f'{artist} добавлен c {res["_id"]}')
    return res.inserted_id


def add_place():
    pass


def add_price():
    pass


def add_date():
    pass


def run():
    filename = 'artists.csv'
    pass


if __name__ == '__main__':
    run()
