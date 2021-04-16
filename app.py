from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

import api

app = Flask("Ing")
api_init = Api(app)
api_init.add_resource(api.Plus, "/plus")

app.config["MONGO_URI"] = "mongodb://localhost:27017/flask-ing"
mongo = PyMongo(app)
collection = mongo.db.tmp


@app.route("/")
def index():

    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)