from flask import Flask,request
from flask_restful import Resource,Api
import json
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'post': '9200'}])
app=Flask(__name__)
api=Api(app)

class Post(Resource):
    def get(self):
        print({"out": es.search(index="bot1", body={"query": {"match": {'question': "ukm"}}})})
        return "1251996"
    def put(self):
        return "vuong"
    def post(self):
        test = dict(request.form)["question"][0]
        return {"out": es.search(index="bot1", body={"query": {"match": {'question': test}}})}

api.add_resource(Post,'/QA')
if __name__ =="__main__":
    # app.run()
    app.run(host='0.0.0.0')