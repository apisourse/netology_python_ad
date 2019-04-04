from pprint import pprint
import csv
import pymongo
from datetime import datetime
import re


def read_csv(filename):
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        next(rows)
        data = list(rows)
        return data


def read_data(data, coll):
    for i in data:
        coll.insert_one({
            'Artist': i[0],
            'Price': float(i[1]),
            'Place': i[2],
            'Data': datetime(2019,
                             round(float(i[3]) % 1 * 100),
                             int(float(i[3])))
        })


def find_cheapest(coll):
    cheapest = coll.find().sort('Price', 1)
    for i in cheapest:
        print(f'{i["Price"]}: {i["Artist"]} в {i["Place"]}')


def find_by_name(name, coll):
    rx = r'.*' + f'{name}' + '.*'
    regex = re.compile(rx)

    find = coll.find().p
    for i in find:
        result = re.match(regex, i['Artist'])
        if result:
            print(f'{i["Artist"]} в {i["Place"]} за {i["Price"]}')


def run():
    # Config
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn['iSourse']
    coll = db['netology_mongo']
    data = read_csv('artists.csv')

    # TODO 0: Delete
    # coll.delete_many({}) # все снести из коллекции

    # TODO 1: импорт данных из csv
    # read_data(data, coll)

    # TODO 2: отсортировать билеты из базы по возрастания цены
    # find_cheapest(coll)

    # TODO 3: отсортировать билеты из базы по возрастания цены
    looking = input("what you're looking for?: ")
    find_by_name(looking, coll)


if __name__ == '__main__':
    run()
