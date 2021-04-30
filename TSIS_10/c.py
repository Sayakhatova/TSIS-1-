#insert data into table

import psycopg2

conn=psycopg2.connect(
    database='mydb',
    user='postgres',
    password='1535',
    #port='5432',
    #host='localhost'
)

cur=conn.cursor()

cur.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)\
    VALUES(1, 'Paul', 32, 'California', 2000.0)");
cur.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)\
    VALUES(2, 'Lola', 22, 'California', 25000.0)");

conn.commit()

conn.close()