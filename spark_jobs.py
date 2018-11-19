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
