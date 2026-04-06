from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ETL_S3_Project") \
    .getOrCreate()

input_path = "s3a://my-etl-orders-bucket-123/input/orders_1000_rows.csv/"
high_path = "s3a://my-etl-orders-bucket-123/output/high_value/"
low_path = "s3a://my-etl-orders-bucket-123/output/low_value/"

df = spark.read.csv(input_path, header=True, inferSchema=True)

completed_df = df.filter(col("order_status") == "Completed")

high_df = completed_df.filter(col("total_amount") >= 10000)
low_df = completed_df.filter(col("total_amount") < 10000)

high_df.write.mode("overwrite").partitionBy("country").parquet(high_path)
low_df.write.mode("overwrite").partitionBy("country").parquet(low_path)

spark.stop()
