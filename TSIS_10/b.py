#create a table

import  psycopg2 

conn=psycopg2.connect(
    database='mydb',
    user='postgres',
    password='1535',
    host='localhost', 
    port='5432'
)

cur=conn.cursor()

cur.execute(
    """
    CREATE TABLE COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);
    """
)

conn.commit()

conn.close()