import psycopg2

conn = None
cur = None
try:
    conn = psycopg2.connect(dbname="postgres",  # information from pg properties
                            user="postgres",
                            password="12345678Aa",
                            host="postgres"
                            )
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRI"
                "MARY KEY, name TEXT, skills VARCHAR);")
    insert_script = "INSERT INTO users (name, skills) VALUES(%s, %s)"
    insert_values = [("John", "driver"), ("Bob", "security"), ("Mary", "boss")]
    for record in insert_values:
        cur.execute(insert_script, record)
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
