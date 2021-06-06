import mysql.connector as connection
import logging as log

class MySQLUtil:
    log.basicConfig(level=log.INFO)

    def __init__(self):
        self.db_conn = self.get_connection()

    def get_connection(self):
        try:
            db_conn = connection.connect(host="localhost",  database='Student', user="root", passwd="*****", use_pure=True,autocommit=True)
            # check if the connection is established
            return db_conn
        except Exception as e:
            log.error(str(e))
            raise e


    def create_table(self,insert_str):
        try:
            cursor = self.db_conn.cursor()  # create a cursor to execute queries
            cursor.execute(insert_str)
        except Exception as e:
            log.error(str(e))
            raise e

    def execute_table_data(self, query_str):
        try:
            cursor = self.db_conn.cursor()  # create a cursor to execute queries
            cursor.execute(query_str)
        except Exception as e:
            log.error(str(e))
            raise e

    def select_table_data(self, query_str):
        try:
            cursor = self.db_conn.cursor()  # create a cursor to execute queries
            cursor.execute(query_str)
            results = cursor.fetchall()
            results[0] = [i[0] for i in cursor.description]
            return results
        except Exception as e:
            log.error(str(e))
            raise e
