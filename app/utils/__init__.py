import os
from minio import Minio
from app.utils.FileHandler import FileHandler

# Initialize Minio client
minio_client = Minio(
    os.getenv("MINIO_SERVER", "localhost:9000"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,
)


bucket_name = "images"


file_handler = FileHandler(minio_client, bucket_name)
