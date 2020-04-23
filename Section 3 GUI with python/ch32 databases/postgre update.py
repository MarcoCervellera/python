import psycopg2

def update(name, mark, rollno):
    conn = psycopg2.connect("dbname='data' user='postgres' password='admin' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=%s, marks=%s  WHERE rollno=%s", (name, mark, rollno))
    conn.commit()
    conn.close()

update("aname", 50, 5)