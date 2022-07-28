"""
Flask App for configuring endpoint to azure storage containers
"""

import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from flask import Flask, jsonify

# connection configurations to azure
load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

app = Flask(__name__)

@app.route('/')
def list_files():

    """
    An api for listing stored files on Azure storage containers.
    _ _ _ 

    tags:
        - Listing File API
    parameters: None
    responses:
        500:
            description: Internal Server Error
            schema:
                status: Error at server!
        200:
            description: API response with filenames
            schema:
                files:
                    type: json
                    description: json response with path to files stored in azure container 
    """

    try:
        # coonect to blob service
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client("container1")
        blob_list = container_client.list_blobs()
        filenames = []
        # store filenames in list
        for blob in blob_list:
            filenames.append(blob.name)
        return jsonify(
            files=filenames
        )
    except Exception:
        return jsonify(
            status="Error at server!",
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
