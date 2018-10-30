import json
from configText import  convert
import mysql.connector
import sys
import requests
from elasticsearch import Elasticsearch

def conf(t):
    if t==None:
        return ""
    else:
        return t

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
    out=[]
    for i in data:
        temp = {}
        d = list(i)
        temp["id"] = i[0]
        temp["question"] = i[1]
        temp["answer"] = i[2]
        out.append(temp)
    res = requests.get("http://localhost:9200/")
    es = Elasticsearch([{'host': 'localhost', 'post': '9200'}])
    for i in range(len(out)):
        es.index(index=name_database, doc_type='qa', id=int(out[i]["id"]), body=out[i])


if __name__ == '__main__':
    put(sys.argv[1],sys.argv[2])