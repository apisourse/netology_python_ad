from pprint import pprint
import csv
import pymongo
from datetime import datetime
import re

# Config
conn = pymongo.MongoClient('localhost', 27017)
db = conn['iSourse']
coll = db['netology_mongo']


def read_csv(filename):
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        next(rows)
        data = list(rows)
        return data


def read_data(data):
    for i in data:
        coll.insert_one({
            'Artist': i[0],
            'Price': float(i[1]),
            'Place': i[2],
            'Data': datetime(2019,
                             round(float(i[3]) % 1 * 100),
                             int(float(i[3])))
        })


def find_cheapest():
    cheapest = coll.find().sort('Price', 1)
    for i in cheapest:
        print(f'{i["Price"]}: {i["Artist"]} в {i["Place"]}')


def find_by_name():
    input_artist = input('Введите название артиста')
    regex = re.compile()

    find = coll.find({'Artist': "Tom"}).sort('Price', 1)


def run():
    filename = 'artists.csv'
    data = read_csv(filename)
    # read_data(data) #импорт данных из csv в mongo
    # coll.delete_many({}) # все снести из коллекции
    # find_cheapest()
    find_by_name()

if __name__ == '__main__':
    run()
