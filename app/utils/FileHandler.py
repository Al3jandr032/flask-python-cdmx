from io import BytesIO
from minio.error import S3Error
from collections import namedtuple

UploadResult = namedtuple("UploadResult", "success status data")
DownloadResult = namedtuple("DownloadResult", "success status data")


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
            writeResult = self.minio_client.put_object(
                self.bucket_name,
                file.filename,
                BytesIO(file_data),
                length=len(file_data),
                content_type=file.content_type,
            )
            result = UploadResult(
                True,
                "File uploaded successfully!",
                {
                    "name": writeResult.object_name,
                    "etag": writeResult.etag,
                    "version_id": writeResult.version_id,
                },
            )
            print(result)
            return result
        except S3Error as e:
            return UploadResult(False, f"Error uploading file: {e}", None)
        except Exception as e:
            return UploadResult(False, f"Unexpected error: {e}", None)

    def download_file(self, name):
        try:
            object_data = None

            with self.minio_client.get_object(self.bucket_name, name) as min_obj:
                object_data = BytesIO(min_obj.read())

            result = DownloadResult(True, "File downloaded successfully!", object_data)
            return result
        except S3Error as e:
            return DownloadResult(False, f"Error uploading file: {e}", None)
        except Exception as e:
            return DownloadResult(False, f"Unexpected error: {e}", None)
