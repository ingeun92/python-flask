from flask import Flask
from flask_pymongo import PyMongo


app = Flask("Ing")


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()