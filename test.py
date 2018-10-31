import mysql.connector
from elasticsearch import Elasticsearch

def put(name_database,name_table):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="okmijnuhb",
        database=name_database
    )
    mycursor = mydb.cursor()
    sql="SELECT * from "+name_table
    mycursor.execute(sql)
    data=mycursor.fetchall()
    print(data)
    # es = Elasticsearch([{'host': 'localhost', 'post': '9200'}])
    # a=es.search(index="b1", body={"query": {"match": {'question':'ai cho em'}}})
    # print(a)

if __name__ == '__main__':
    put("b1","qa")
    put("bot1","qa")