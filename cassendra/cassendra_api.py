from flask import Flask, render_template, request, jsonify,Blueprint
from cassendra.cassendra_db import CassendraUtil
import logging as log
import csv

log.basicConfig(level=log.INFO)
cassendra_api = Blueprint('cassendra_api', __name__)

cassendra_util = CassendraUtil()

@cassendra_api.route('/cassendra/create_table',methods=['POST'])
def cassendra_create_table():
     try:
         table_name = request.json['table_name']
         columns = request.json['columns']
         data_types = request.json['data_types']

         insert_query = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)

         for i in range(0,len(columns)):
             insert_query += columns[i] + " " + data_types[i]
             if(i< len(columns) -1):
                 insert_query += ","
             else:
                 insert_query += ")"

         log.info("Insert Query:- " + insert_query)
         cassendra_util.execute_table_data(insert_query)
         return "Table Created Successfully"
     except Exception as e:
       log.error(str(e))
       return "Error Creating Table"

@cassendra_api.route('/cassendra/insert_table_data', methods=['POST'])
def cassendra_insert_table_data():
    try:
     table_name = request.json['table_name']
     columns = request.json['columns']
     values = request.json['values']

     insert_query = "INSERT INTO {} (".format(table_name)
     for i in range(0, len(columns)):
         insert_query += columns[i]
         if (i < len(columns) - 1):
             insert_query += ","
         else:
             insert_query += ") VALUES ("
     for i in range(0, len(values)):
         insert_query += "'" + values[i] + "'"
         if (i < len(values) - 1):
             insert_query += ","
         else:
             insert_query += ")"

     log.info("Insert Query:- " + insert_query)
     cassendra_util.execute_table_data(insert_query)
     return "Record inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Inserting  Record"

@cassendra_api.route('/cassendra/update_table_data', methods=['POST','PUT'])
def cassendra_update_table_data():
    try:
        table_name = request.json['table_name']
        columns = request.json['columns']
        values = request.json['values']
        condition = request.json['condition']

        update_query = "UPDATE {} SET ".format(table_name)
        for i in range(0, len(columns)):
            update_query += columns[i] + " = " + "'" + values[i] + "'"
            if (i < len(columns) - 1):
                update_query += ","

        update_query += " " + condition
        log.info("Update Query :- " + update_query)

        cassendra_util.execute_table_data(update_query)
        return "Records Updated Successfully"

    except Exception as e:
        log.error(str(e))
        return "Error Updating  Record"

@cassendra_api.route('/cassendra/delete_table_data', methods=['POST','DELETE'])
def cassendra_delete_table_data():
    try:
        table_name = request.json['table_name']
        condition = request.json['condition']

        delete_query = "DELETE FROM {} {} ".format(table_name,condition)
        log.info("Update Query :- " + delete_query)

        cassendra_util.execute_table_data(delete_query)
        return "Records Deleted Successfully"

    except Exception as e:
        log.error(str(e))
        return "Error Deleting Record"

@cassendra_api.route('/cassendra/bulk_insert_data', methods=['POST'])
def cassendra_bulk_insert_table_data():
    try:
        table_name = request.json['table_name']
        file_name = request.json['file_name']
        bulk_insert_query = "INSERT INTO {} ".format(table_name)
        line_count = 0
        with open(file_name, "r") as f:
            table_data = csv.reader(f, delimiter="\n")
            for line in enumerate(table_data):
                if line_count == 0:
                    bulk_insert_query += "(" + f'{", ".join(line[1])}' + ") values "
                    line_count += 1
                else:
                    for list_ in (line[1]):
                        log.info("Bulk Insert Query: " + bulk_insert_query + "({})".format(list_))
                        cassendra_util.execute_table_data(bulk_insert_query + "({})".format(list_))
                        line_count += 1
        return "Records Inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Bulk Insertion of  Record"

@cassendra_api.route('/cassendra/view_table_data', methods=['POST'])
def cassendra_view_table_data():
    try:
        table_name = request.json['table_name']
        select_query = "select * from {}".format(table_name)
        results = cassendra_util.select_table_data(select_query)

        filename = "cassendra/cassendra_download_records.csv"
        with open(filename, 'w') as f:
            # creating a csv writer object
            csvwriter = csv.writer(f)

            # writing the data rows
            csvwriter.writerows(results)

        return "Records Downloaded Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Download of   Record"
