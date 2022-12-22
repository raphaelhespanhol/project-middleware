import logging
import json

import azure.functions as func

def main(myblob: func.InputStream, 
         msgOutQueue: func.Out[func.QueueMessage]):
    logging.info(
        f"Python blob trigger function processed blob \n"
        f"Name: '{myblob.name}'\n"
        f"URI: '{myblob.uri}'\n"
        f"Blob Size: '{myblob.length}' bytes"
    )

    json = myblob.readline()
    
    if (_validateJSON(json)):
        logging.info(f"Sending to queue a new message with: '{json}'")
        msgOutQueue.set(json.decode('utf-8'))
    
def _validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        logging.error("An invalid json was sent! Please verify!")
        return False

    logging.info("Json validaded with success!")
    return True