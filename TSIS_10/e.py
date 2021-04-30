#update data in table

import psycopg2

conn=psycopg2.connect(
    database='mydb',
    user='postgres',
    password='1535'
)

cur=conn.cursor()

cur.execute("UPDATE COMPANY set AGE=20 where ID=1")

conn.commit()

cur.execute('SELECT * from COMPANY')

rows=cur.fetchall()

for row in rows:
    print('ID=', row[0])
    print('NAME=', row[1])
    print('AGE=', row[2])
    print('ADDRESS=', row[3])
    print('SALARY=', row[4], '\n')

conn.close()