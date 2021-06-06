from cassandra.cluster import Cluster
import logging as log

class CassendraUtil:
    log.basicConfig(level=log.INFO)

    def __init__(self)
        self.db_conn = self.get_connection()

    def get_connection(self):
        try:
            clstr = Cluster()
            db_conn = clstr.connect('my_db')
            return db_conn
        except Exception as e:
            log.error(str(e))
            raise e

    def execute_table_data(self, query_str):
        try:
            self.db_conn.execute(query_str)
        except Exception as e:
            log.error(str(e))
            raise e

    def select_table_data(self, query_str):
        try:
            rows = self.db_conn.execute(query_str)
            return rows
        except Exception as e:
            log.error(str(e))
            raise e
