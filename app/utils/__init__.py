import os
from minio import Minio
from app.utils.file_handler import FileHandler

# Initialize Minio client
minio_client = Minio(
    os.getenv("MINIO_SERVER", "localhost:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,
)
BUCKET_NAME = "images"
file_handler = FileHandler(minio_client, BUCKET_NAME)
