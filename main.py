import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from flask import Flask, jsonify

load_dotenv()
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

app = Flask(__name__)

@app.route('/')
def list_files():
    try: 
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client("container1")
        blob_list = container_client.list_blobs()
        filenames = []  
        for blob in blob_list:
            filenames.append(blob.name)
        return jsonify(
            files=filenames
        )
    except Exception as ex:
        return jsonify(
            status="Error at server!"
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0')