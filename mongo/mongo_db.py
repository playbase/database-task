import pymongo
import logging as log

class MongoUtil:
       log.basicConfig(level=log.INFO)

       def __init__(self):
              self.db_conn = self.get_connection("first_db","emp")

       def get_connection(self,db_name, col_name):
              try:
                   conn = pymongo.MongoClient("localhost", 27017)
                   return conn[db_name][col_name]
              except Exception as e:
                     log.error(str(e))
                     raise e

       def insert_collection_data(self, insert_str):
           try:
               self.db_conn.insert_one(insert_str)
           except Exception as e:
               log.error(str(e))
               raise e

       def update_collection_data(self, query_str,value_str):
           try:
               self.db_conn.update_many(query_str, value_str)
           except Exception as e:
               log.error(str(e))
               raise e

       def delete_collection_data(self, query_str):
           try:
               self.db_conn.delete_many(query_str)
           except Exception as e:
               log.error(str(e))
               raise e

       def insert_bulk_collection_data(self, insert_str):
           try:
               self.db_conn.insert_many(insert_str)
           except Exception as e:
               log.error(str(e))
               raise e

       def select_collection_data(self):
           try:
               return self.db_conn.find()
           except Exception as e:
               log.error(str(e))
               raise e