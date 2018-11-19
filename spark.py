from pyspark.sql import SparkSession
from functools import lru_cache
from settings import *


@lru_cache(maxsize=None)
def get_spark():
    return (SparkSession.builder
                .master(MASTER)
                .appName("demo_api_spark")
                .getOrCreate())
