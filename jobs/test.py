from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NYC Taxi Analysis") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minio") \
    .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .getOrCreate()
    #.master("spark://spark-master:7077") \


# Set log level to WARN to reduce unnecessary logs
#spark.sparkContext.setLogLevel("WARN")
spark

df = spark.read.parquet("s3a://mybucket/taxi/input/NYC-Taxi.parquet")
df.cache()

result = df.groupBy("passenger_count").count()
result.show()
print(result.count())
result.write.mode("overwrite").parquet("s3a://mybucket/taxi/output")
result.write.mode("overwrite").parquet("/opt/spark/data/output")
print("SuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuCCeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeSS!! :)")


spark.stop()
