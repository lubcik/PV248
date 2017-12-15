import json
import sqlite3
import sys

conn = sqlite3.connect('scorelib.dat')
cur = conn.cursor()
cur.execute("select * from person")
data = cur.fetchall()
conn.commit()

# pretty print to stdout
json.dump(data, sys.stdout, indent=4)