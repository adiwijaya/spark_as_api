from datetime import datetime
import findspark

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#SPARK INIT
findspark.init()
from spark import get_spark
spark_session = get_spark()
sc = spark_session.sparkContext

def count_length(string):
    list_string = list(string)
    rdd = sc.parallelize(list_string)
    count = rdd.count()
    return count

def read_table(table_name):
    import pandas as pd
    result = spark.sql("SELECT * FROM %s"%table_name)
    pandas_df = df.toPandas()
    json_result = pandas_df.to_json
    return json_result
