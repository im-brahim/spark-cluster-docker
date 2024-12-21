from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NYC Taxi Analysis").getOrCreate()


# Set log level to WARN to reduce unnecessary logs
# spark.sparkContext.setLogLevel("WARN")

# df = spark.read.parquet("s3a://mybucket/taxi/input/NYC-Taxi.parquet")
# df.cache()

# result = df.groupBy("passenger_count").count()
# result.show()
# print(result.count())

# result.write.mode("overwrite").parquet("s3a://mybucket/taxi/output")     # df.coalesce(1)
# result.write.mode("overwrite").parquet("/opt/spark/data/output")

# df = spark.read.parquet("s3a://mybucket/taxi/output")
# df = spark.read.parquet("/opt/spark/data/output")
# df.show()



print("SuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuCCeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeSS!! :)")
spark.stop()
