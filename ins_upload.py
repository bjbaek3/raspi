import pymysql
import ftplib
import datetime 
import time
#from shutil import copyfile 
#import os


db=pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')

i = 1
while i <= 10:

    cur = db.cursor()

    now = datetime.datetime.now()
    photoname = 'photo' + str(now.year) + str(now.month) + str(now.hour) + str(now.minute) + str(now.second) + str(now.microsecond)


    cur.execute("INSERT INTO photolog(yyyymmdd, photoname, flag) VALUES (NOW(), '" + photoname + "', 1) ")
    db.commit()


    with ftplib.FTP(host='oldmansea.synology.me') as ftp:
        ftp.set_pasv(False)
        ftp.login(user='51050072', passwd='11')
        ftp.cwd('./php/img')
        
     #   copyfile('img02.png', 'img_ftp.png')
     #   os.chmod('img_ftp.png', 0o0777)
     #   time.sleep(3)
 
    with open('img02.png', 'rb') as read_f:
            ftp.storbinary("STOR " + photoname + ".png", read_f)
    
    #if os.path.exists('img_ftp.png'):
    #     os.remove('img_ftp.png')

    time.sleep(10)
    i = i + 1

db.close()

