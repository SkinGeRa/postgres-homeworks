import csv

import psycopg2

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="1231314454qwe")
try:
    with conn:
        with conn.cursor() as cur:
            with open('../homework-1/north_data/customers_data.csv', 'r', encoding="utf-8") as file:
                item = csv.reader(file)
                next(item)
                for line in item:
                    cur.execute("INSERT INTO customers VALUES(%s, %s, %s)", (line[0], line[1],
                                                                             line[2]))
            with open('../homework-1/north_data/employees_data.csv', 'r', encoding="utf-8") as file:
                item = csv.reader(file)
                next(item)
                for line in item:
                    cur.execute("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)", (line[0], line[1],
                                                                                         line[2], line[3],
                                                                                         line[4], line[5]))
            with open('../homework-1/north_data/orders_data.csv', 'r', encoding="utf-8") as file:
                item = csv.reader(file)
                next(item)
                for line in item:
                    cur.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)", (line[0], line[1],
                                                                                  line[2], line[3],
                                                                                  line[4]))

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Ошибка: {error}")

finally:
    conn.close()
