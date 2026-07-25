import os
from pyspark.sql import SparkSession


def get_spark(app_name: str) -> SparkSession:
    return (
        SparkSession.builder.appName(app_name)
        .master("spark://spark-master:7077")
        .config("spark.hadoop.fs.s3a.endpoint", os.getenv("B2_ENDPOINT"))
        .config("spark.hadoop.fs.s3a.endpoint.region", os.getenv("B2_REGION"))
        .config("spark.hadoop.fs.s3a.access.key", os.getenv("B2_ACCESS_KEY"))
        .config("spark.hadoop.fs.s3a.secret.key", os.getenv("B2_SECRET_KEY"))
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .getOrCreate()
    )