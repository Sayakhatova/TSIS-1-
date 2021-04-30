#select from table

import psycopg2

conn=psycopg2.connect(
    database='mydb',
    user='postgres',
    password='1535'
)

cur=conn.cursor()

cur.execute("SELECT id, name, address, salary from COMPANY")

rows=cur.fetchall()
for row in rows:
    print('ID=', row[0])
    print('NAME=', row[1])
    print('ADDRESS=', row[2])
    print('SALARY=', row[3], '\n')

conn.close()