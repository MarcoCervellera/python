import psycopg2

def delete(rollno):
    conn = psycopg2.connect("dbname='data' user='postgres' password='admin' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data  WHERE rollno=%s", (rollno,))
    conn.commit()
    conn.close()

delete(5)