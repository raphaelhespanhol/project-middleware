import logging
import json
import os
import azure.functions as func

from helper.azure_helper import AzureHelper

def main(myblob: func.InputStream, 
         msgOutQueue: func.Out[func.QueueMessage],
         outProcessedBlob: func.Out[str],
         outErrorBlob: func.Out[str]):
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
        outProcessedBlob.set(json)
    else:
        outErrorBlob.set(json)
    
    azure = AzureHelper(myblob.name)
    azure.delete_blob()
    
def _validateJSON(jsonData):
    try:
        if (len(jsonData) < 4):
            raise ValueError()

        json.loads(jsonData)
    except ValueError as err:
        logging.error("An invalid json was sent! Please verify!")
        return False

    logging.info("Json validaded with success!")
    return True