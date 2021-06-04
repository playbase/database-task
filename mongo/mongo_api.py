from flask import Flask, render_template, request, jsonify,Blueprint
from mongo.mongo_db import MongoUtil
import logging as log
import csv

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
        with open(file_name, "r") as f:
            table_data = csv.reader(f, delimiter="\n")
            for line in enumerate(table_data):
                if line_count == 0:
                    line_count += 1
                else:
                    for list_ in (line[1]):
                        log.info("Bulk Insert Query: {}".format(jsonify(list_)))
                        ##mongo_util.execute_table_data(bulk_insert_query + "({})".format(list_))
                        line_count += 1
        return "Records Inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Bulk Insertion of  Record"