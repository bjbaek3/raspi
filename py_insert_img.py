#import mysql.connector
#from mysql.connector import Error

import pymysql

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(number, name, photo):
    print("Inserting BLOB into images table")
    try:
        connection = pimysql.connect(host='oldmansea.synology.me',
                                             database='oldman',
                                             user='root',
                                             password='Fyeo2014!@#')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO photolog
                          (yyyymmdd, photo, flag) VALUES (%s,%s,%s)"""

        Picture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (yyyymmdd, photo, flag) 
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple) 
        connection.commit()
        print("Image and file inserted successfully as a BLOB into images table", result)

   # except mysql.connector.Error as error:
   #     print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
   #     if (connection.is_connected()):
   #         cursor.close()
   #         connection.close()
   #         print("MySQL connection is closed")

insertBLOB(None, "test1", "img01.bmp")
insertBLOB(None, "test2", "img02.png")