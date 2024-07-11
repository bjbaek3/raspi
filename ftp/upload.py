import ftplib

with ftplib.FTP(host='oldmansea.synology.me') as ftp:
    ftp.set_pasv(False)
    ftp.login(user='51050072', passwd='11')
    ftp.cwd('./php/img')
 
    with open('../img01.bmp', 'rb') as read_f:
       # ftp.storlines("STOR img02.png", read_f)
        ftp.storbinary("STOR img02.bmp", read_f)
 
        
   # FTP 서버의 data.txt 파일을 로컬 PC의 data.txt 파일로 다운로드한다.
   # with open('data.txt', 'w') as save_f:
   #     ftp.retrlines("RETR data.txt", save_f.write)

    # data.txt 파일을 읽어 평균을 계산한다.
    #with open('data.txt') as f:
    #    data = f.read()
    #    numbers = data.split()
    #    avg = sum(map(int, numbers)) / len(numbers)

    # 평균을 result.txt 파일에 기록한다.
    #with open('result.txt', 'w') as f:
    #    f.write(str(avg))

    # result.txt 파일을 FTP 서버에 업로드한다.
 

