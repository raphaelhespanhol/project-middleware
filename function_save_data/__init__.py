import logging

import azure.functions as func
from helper.database_helper import DatabaseHelper

def main(msgInQueue: func.QueueMessage):

     logging.info("A new message was added in queue")
     try:
          data = msgInQueue.get_json()
          database = DatabaseHelper()
          database.insert_status(data)
     except:
          logging.error("The message cannot be processed! Please verify it again!")