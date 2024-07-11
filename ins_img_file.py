
# import mysql.connector
import pymysql
import base64
import io
import ftplib
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


with ftplib.FTP(host='oldmansea.synology.me') as ftp:
    ftp.set_pasv(False)
    ftp.login(user='51050072', passwd='11')
    ftp.cwd('./php/img')
 
    with open('../img01.bmp', 'rb') as read_f:
        ftp.storbinary("STOR img02.bmp", read_f)