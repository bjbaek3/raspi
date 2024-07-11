
# import mysql.connector
import pymysql
import base64
import io

import PIL.Image

with open('/home/raspi/python/img02.png', 'rb') as f:
    photo = f.read()
encodestring = base64.b64encode(photo)
db= pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')
cur1=db.cursor()
sql = "insert into photolog(yyyymmdd, photo) values(NOW(),%s)"
i = 1
while i <= 10:
    cur1.execute(sql,(encodestring,))
    i += 1
    db.commit()


db.close()