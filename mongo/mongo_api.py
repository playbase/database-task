from flask import Flask, render_template, request, jsonify,Blueprint
from mongo.mongo_db import MongoUtil
import logging as log
import csv
import json


log.basicConfig(level=log.INFO)
mongo_api = Blueprint('mongo_api', __name__)

mongo_util = MongoUtil()

@mongo_api.route('/mongo/insert_table_data', methods=['POST'])
def mongo_insert_table_data():
    try:
     insert_str = request.json
     log.info("Insert String:- " + str(insert_str))
     mongo_util.insert_collection_data(insert_str)
     return "Record inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Inserting  Record"

@mongo_api.route('/mongo/update_table_data', methods=['POST'])
def mongo_update_table_data():
    try:
     query_str = request.json['query_str']
     value_str = request.json['value_str']
     log.info("Update String:- " + str(query_str) + "," + str(value_str))
     mongo_util.update_collection_data(query_str,value_str)
     return "Record updated Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Updating  Record"

@mongo_api.route('/mongo/delete_table_data', methods=['POST'])
def mongo_delete_table_data():
    try:
     delete_str = request.json
     log.info("Delete String:- " + str(delete_str))
     mongo_util.delete_collection_data(delete_str)
     return "Record deleted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Deleting Record"


@mongo_api.route('/mongo/bulk_insert_data', methods=['POST'])
def mongo_bulk_insert_table_data():
    try:
        file_name = request.json['file_name']
        line_count = 0
        jsonArray = []
        with open(file_name, "r") as f:
            csvReader = csv.DictReader(f)
            for row in csvReader:
                # add this python dict to json array
                jsonArray.append(row)
        log.info("JSON ARR" + str(jsonArray) )
        mongo_util.insert_bulk_collection_data(jsonArray)
        return "Records Inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Bulk Insertion of  Record"

@mongo_api.route('/mongo/view_table_data', methods=['POST'])
def mysql_view_table_data():
    try:
        table_name = request.json['table_name']
        results = mongo_util.select_collection_data()

        log.info("Results" + str(results))

        filename = "mongo/mongo_download_records.csv"
        with open(filename, 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(list(results), default=str)
            jsonf.write(jsonString)

        return "Records Downloaded Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Download of   Record"