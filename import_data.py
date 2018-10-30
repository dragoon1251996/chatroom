import mysql.connector
import sys
import json
def import_data_(name_database,name_table,file_data):
    data=[x.replace("\n","") for x in open(file_data,encoding="utf-8").readlines() if(x.replace("\n","").replace(" ","")!="")]
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=name_database
    )
    mycursor = mydb.cursor()
    q = []
    a = ""
    for x in range(3,len(data)):
        if x%5 == 0:
            a=data[x]
            q=data[x-4:x-1]
            # sql="INSERT INTO "+name_table+" (question,answer) VALUES (" + q[0]+","+a+")"
            sql = "INSERT INTO qa (question,answer) VALUES (%s, %s)"
            val = (" ".join(q), a)
            mycursor.execute(sql, val)

if __name__ == '__main__':
    import_data_(sys.argv[1],sys.argv[2],sys.argv[3])



