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
        chatbot_name = list(dict(request.form).keys())[0]
        body=json.loads(list(dict(request.form).values())[0][0])
        print(body)
        size = es.search(index=chatbot_name, body={"fields": ["id"], "query": {"match_all": {}}})["hits"]["total"]
        es.index(index=chatbot_name, doc_type='qa', id=int(size+1), body={"id":size+1,"question":convert(body["question"]),"answer":convert(body["answer"])})
        return "Train access"

    def post(self):
        try:
            # chatbot_name=list(dict(request.form).keys())[0]
            # print(chatbot_name)
            # test = dict(request.form)[chatbot_name][0]
            return {"answer": [x["_source"]["answer"] for x in es.search(index="chatbot01", body={"query": {"match": {'question': "vkl nhe"}}})["hits"]["hits"]]}
        except Exception as e:
            return str(e) +str(request.form)
api.add_resource(Post,'/QA')

if __name__ =="__main__":
    # app.run()
    app.run(host='0.0.0.0')