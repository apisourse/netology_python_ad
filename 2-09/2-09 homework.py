from pprint import pprint
import csv
import pymongo
from datetime import datetime

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
        print(i['Price'], i['Artist'])


def run():
    filename = 'artists.csv'
    data = read_csv(filename)
    # read_data(data) #импорт данных из csv в mongo
    # coll.delete_many({}) # все снести из коллекции
    # find_cheapest()

if __name__ == '__main__':
    run()
