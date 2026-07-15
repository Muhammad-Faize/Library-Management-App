import psycopg2
import psycopg2.extras

host="localhost"
dbname="LibraryDatabase"
user="postgres"
password="009099"
port=5434


def connection():
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return conn,cur