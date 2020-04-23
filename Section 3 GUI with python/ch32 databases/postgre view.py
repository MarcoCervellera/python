import psycopg2

def view():
    conn = psycopg2.connect("dbname='data' user='postgres' password='admin' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    #memorizza i risultati della query nella variabile
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

print(view())