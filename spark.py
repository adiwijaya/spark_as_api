import findspark
findspark.init()

from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from functools import lru_cache
from settings import *

@lru_cache(maxsize=None)
def get_spark():
    APP_NAME = "demo_api_spark"
    spark_conf = (SparkConf()
    .setAppName(APP_NAME)
    .setMaster(MASTER)
    )

    spark_conf.set("spark.executor.memory", "600M")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    return (spark)

def terminate_spark():
    import pandas as pd
    from spark import get_spark
    spark_session = get_spark()
    spark_session.stop()
