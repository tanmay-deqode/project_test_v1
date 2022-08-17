from pyspark.sql import SparkSession

import pandas as pd
# from API_DataFetch import *
# class ProcessingData:

#     def __init__(self):

#         pass

#     def spark_session(self):
#             spark = SparkSession \
#                 .builder \
#                 .appName("DET- Problem Statement") \
#                 .master("local[*]") \
#                 .getOrCreate() \


#     def df_reader(self):
#         df = spark.read.option("header", "true").option("inferschema", "true").json("helper/demo.json").show()


#             # df = spark.read.option("multiline", "true").option("inferschema", "true").json("helper/demo.json").show()


spark = SparkSession \
    .builder \
    .appName("DET- Problem Statement") \
    .master("local[*]") \
    .getOrCreate() \



df = spark.read.option("header", "true").option(
    "inferschema", "true").csv("data/test_df.csv")

df.show()

dfnew = df.toPandas()
newdf = dfnew.drop_duplicates(keep=False, inplace=True)
# newdf1 = pd.json_normalize(newdf, max_level = 1)

#writer = newdf1.write.format("bigquery").option("table","test_df").mode("overwrite").save()

# df = spark.read.option("multiline", "true").option("inferschema", "true").json("helper/demo.json").show()
