#import pymysql
#db=pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')
#cur = db.cursor()
#cur.execute("INSERT INTO photolog(yyyymmdd,photo,flag) VALUES (NOW(), LOAD_FILE('/home/raspi/python/img02.png'),1) ")
#db.commit()
#db.close()
 

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
while i <= 1000:
    cur1.execute(sql,(encodestring,))
    i += 1
    db.commit()

#with open('/home/raspi/python/img01.bmp', 'rb') as f:
#    photo = f.read()
#encodestring = base64.b64encode(photo)
#db= pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')
#cur2=db.cursor()
#sql = "insert into photolog(yyyymmdd, photo) values(NOW(),%s)"
#cur2.execute(sql,(encodestring,))
#db.commit()



#sql1="select * from photolog"
#mycursor.execute(sql1)
#data = mycursor.fetchall()
#data1=base64.b64decode(data[0][0])
#file_like=io.BytesIO(data1)
#img=PIL.Image.open(file_like)
#img.show()


db.close()