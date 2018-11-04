from flask import Flask,request
from flask_restful import Resource,Api
import json
from elasticsearch import Elasticsearch
from configText import  convert

es = Elasticsearch([{'host': 'localhost', 'post': '9200'}])
app=Flask(__name__)
api=Api(app)

class Post(Resource):
    def get(self):
        return "1251996"
    def put(self):
        return "vuong"
    def post(self):
        chatbot_name=list(dict(request.form).keys())[0]
        print(chatbot_name)
        test = dict(request.form)[chatbot_name][0]
        return {"answer": [x["_source"]["answer"] for x in es.search(index=chatbot_name, body={"query": {"match": {'question': convert(test)}}})["hits"]["hits"]]}

api.add_resource(Post,'/QA')

if __name__ =="__main__":
    # app.run()
    app.run(host='0.0.0.0')