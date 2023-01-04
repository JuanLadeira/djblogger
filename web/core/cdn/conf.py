import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "djblog-project"
AWS_S3_ENDPOINT_URL = "https://sfo3.digitaloceanspaces.com"
AWS_S3_OBJECTS_PAREMETERS = {"CacheControl": "max-age=86400", "ACL": "public-read"}
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_LOCATION = "https://djblog-project.sfo3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "core.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "core.cdn.backends.StaticRootS3BotoStorage"
