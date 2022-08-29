from pyspark.sql import SparkSession

import sys
import pandas as pd


class ProcessingData:

    spark = spark_session()

    def __init__(self):

        master: str = sys.argsv[0]
        filetype: str = sys.argv[1]

    def spark_session(self):
        spark = SparkSession \
            .builder \
            .appName("DET- Problem Statement") \
            .master(self.master) \
            .getOrCreate() \


    def df_reader(self):
        df = spark.read.option("header", "true").option(
            "inferschema", "true").json("helper/demo.json").show()
