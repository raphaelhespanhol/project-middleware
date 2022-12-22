import logging

import azure.functions as func

def main(msgInQueue: func.QueueMessage):
    logging.info(f"Loaded the message: '{msgInQueue.get_body}'")