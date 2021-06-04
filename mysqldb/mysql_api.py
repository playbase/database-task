from flask import Flask, render_template, request, jsonify,Blueprint
from mysqldb.mysql_db import MySQLUtil
import logging as log
import csv

log.basicConfig(level=log.INFO)
mysql_api = Blueprint('mysql_api', __name__)

mysql_util = MySQLUtil()

@mysql_api.route('/mysqldb/create_table',methods=['POST'])
def mysql_create_table():
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
         mysql_util.create_table(insert_query)
         return "Table Created Successfully"
     except Exception as e:
       log.error(str(e))
       return "Error Creating Table"

@mysql_api.route('/mysqldb/insert_table_data', methods=['POST'])
def mysql_insert_table_data():
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
     mysql_util.execute_table_data(insert_query)
     return "Record inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Inserting  Record"

@mysql_api.route('/mysqldb/update_table_data', methods=['POST','PUT'])
def mysql_update_table_data():
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

        mysql_util.execute_table_data(update_query)
        return "Records Updated Successfully"

    except Exception as e:
        log.error(str(e))
        return "Error Updating  Record"

@mysql_api.route('/mysqldb/delete_table_data', methods=['POST','DELETE'])
def mysql_delete_table_data():
    try:
        table_name = request.json['table_name']
        condition = request.json['condition']

        delete_query = "DELETE FROM {} {} ".format(table_name,condition)
        log.info("Update Query :- " + delete_query)

        mysql_util.execute_table_data(delete_query)
        return "Records Deleted Successfully"

    except Exception as e:
        log.error(str(e))
        return "Error Deleting Record"

@mysql_api.route('/mysqldb/bulk_insert_data', methods=['POST'])
def mysql_bulk_insert_table_data():
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
                        mysql_util.execute_table_data(bulk_insert_query + "({})".format(list_))
                        line_count += 1
        return "Records Inserted Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Bulk Insertion of  Record"

@mysql_api.route('/mysqldb/view_table_data', methods=['POST'])
def mysql_view_table_data():
    try:
        table_name = request.json['table_name']
        select_query = "select * from {}".format(table_name)
        results = mysql_util.select_table_data(select_query)

        filename = "mysqldb/mysql_download_records.csv"
        with open(filename, 'w') as f:
            # creating a csv writer object
            csvwriter = csv.writer(f)

            # writing the data rows
            csvwriter.writerows(results)

        return "Records Downloaded Successfully"
    except Exception as e:
        log.error(str(e))
        return "Error Download of   Record"
