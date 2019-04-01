import psycopg2
from pprint import pprint

with psycopg2.connect(database='postgres', user='artempakhomov', password='milk0990', host='localhost') as conn:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM product_shop')
        pprint(curs.fetchall()) # Вывести все
        # curs.fetchone()) # Вывести построчно

# conn.rollback() # Не применять изменения
# conn.commit() # применить изменения