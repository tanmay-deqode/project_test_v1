from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession \
    .builder \
    .appName("DET- Problem Statement") \
    .master("local[*]") \
    .getOrCreate() \

x = "data/testData.json"

df = pd.read_json(x)
# df = spark.read.option("header", "true").option(
#     "inferschema", "true").csv(x)

x1 = pd.json_normalize(df, max_level=1)
