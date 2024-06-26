import pymysql
import sys

n = len(sys.argv)

db=pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')
cur = db.cursor()
cur.execute("SELECT * FROM helloworld")
rows = cur.fetchall()

for x in rows:
  print(x)

db.close()
 