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
    print('OK! Data imported.')


def find_cheapest(coll):
    cheapest = coll.find().sort('Price', 1)
    for i in cheapest:
        f = f'{i["Price"]}: {i["Artist"]} в {i["Place"]}'
        yield f


def find_by_name(name, coll):
    rx = r'.*' + f'{name}' + '.*'
    regex = re.compile(rx, re.I)

    find = coll.find()
    for i in find:
        result = re.match(regex, i['Artist'])
        if result:
            f = f'{i["Artist"]} в {i["Place"]} за {i["Price"]} фантиков'
            yield f


def run():
    # Config
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn['iSourse']
    coll = db['netology_mongo']
    data = read_csv('artists.csv')

    # TODO 0:
    # coll.delete_many({})

    # TODO 1: импорт данных из csv
    # read_data(data, coll)
    # for i in coll.find():
    #     print(i)
    #
    # TODO 2: отсортировать билеты из базы по возрастания цены
    # for i in find_cheapest(coll):
    #     print(i)

    # TODO 3: найти билеты по исполнителю, где имя исполнителя может быть задано не полностью
    looking = input("what you're looking for?: ")
    for i in find_by_name(looking, coll):
        print(i)


if __name__ == '__main__':
    run()
