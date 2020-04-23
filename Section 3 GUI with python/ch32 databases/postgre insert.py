import psycopg2

def insertdata(roleno, name, mark):
    conn = psycopg2.connect("dbname='data' user='postgres' password='admin' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s, %s, %s)",(roleno, name, mark))
    conn.commit()
    conn.close()

insertdata(5 , 'puggi', 100.0)