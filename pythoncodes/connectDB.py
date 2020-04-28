import psycopg2
conn = psycopg2.connect("host='172.20.0.2' port='5432' dbname='testdb' user='weetong' password='postgres'")
cur = conn.cursor()

cur.execute("""CREATE TABLE logs(
        firstname text,
        lastname text,
        price text,
        spending text
)
""")
conn.commit()

"""
filepath = "/opt/flask-app/04-16-2020_Dataset.csv"

with open(filepath,'r') as f:
    next(f)
    cur.copy_from(f,'firstName'
print("success")
"""
