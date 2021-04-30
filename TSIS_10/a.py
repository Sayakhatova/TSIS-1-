#connect to database

import  psycopg2 

conn=psycopg2.connect(
    database='mydb',
    user='postgres',
    password='1535',
    host='localhost', 
    port='5432'
)

conn.close()