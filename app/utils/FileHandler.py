from io import BytesIO
from minio.error import S3Error


class FileHandler:
    def __init__(
        self,
        minio_client,
        bucket_name,
        allowed_extensions={"png", "jpg", "jpeg", "gif"},
    ):
        self.minio_client = minio_client
        self.bucket_name = bucket_name
        self.allowed_extensions = allowed_extensions

    def allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in self.allowed_extensions
        )

    def upload_file(self, file):
        try:
            # Check if the file has an allowed extension
            if not self.allowed_file(file.filename):
                return {"error": "File type not allowed"}, 400

            file_data = file.read()

            # Make the bucket if it doesn't exist.
            found = self.minio_client.bucket_exists(self.bucket_name)
            if not found:
                self.minio_client.make_bucket(self.bucket_name)
                print("Created bucket", self.bucket_name)
            else:
                print("Bucket", self.bucket_name, "already exists")

            # Upload the file data to Minio
            self.minio_client.put_object(
                self.bucket_name,
                file.filename,
                BytesIO(file_data),
                length=len(file_data),
                content_type=file.content_type,
            )

            return {"message": "File uploaded successfully!"}, 201
        except S3Error as e:
            return {"error": f"Error uploading file: {e}"}, 500
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}, 500
