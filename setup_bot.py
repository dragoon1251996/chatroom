
import mysql.connector
import sys
def CreaateDataBaseBot(name_database):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="okmijnuhb"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS "+name_database)

def CreatTableBot(name_database,name_table):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="okmijnuhb",
        database=name_database
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS "+name_table+" (id INT AUTO_INCREMENT PRIMARY KEY, question TEXT CHARACTER SET utf8,  answer TEXT CHARACTER SET utf8)")




if __name__ == '__main__':
    CreaateDataBaseBot(sys.argv[1])
    CreatTableBot(sys.argv[1],sys.argv[2])