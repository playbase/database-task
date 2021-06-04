from flask import Flask, render_template, request, jsonify,Blueprint
from mysqldb.mysql_api import mysql_api
from mongo.mongo_api import mongo_api
from cassendra.cassendra_api import cassendra_api

app = Flask(__name__)
app.register_blueprint(mysql_api)
app.register_blueprint(mongo_api)
app.register_blueprint(cassendra_api)

@app.route('/', methods=['GET'])  # To render Homepage
def home_page():
    return "Welcome !!"

## For running the app.
if __name__ == '__main__':
    app.run()
