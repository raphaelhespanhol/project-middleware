import logging
import os
from azure.storage.blob import ContainerClient

class AzureHelper:
    def __init__(self, blob):
        blob = blob.split("/")
        self.container = blob[0]
        self.folder = blob[1]
        self.file = blob[2]
        self.container_client = ContainerClient.from_connection_string(conn_str=os.getenv("AZURE_STORAGE_CONNECTION_STRING"), container_name=self.container)
        
    def delete_blob(self):
        path = self.folder+"/"+self.file
        logging.warn(f"Deleting blob: '{path}'")
        try:
            self.container_client.delete_blob(blob=path)
            logging.info("File deleted with success!")
        except:
            logging.error(f"Error to delete blob file: '{self.file}'")