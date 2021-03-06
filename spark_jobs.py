def count_length(string):
    from spark import get_spark
    spark_session = get_spark()

    sc = spark_session.sparkContext
    list_string = list(string)
    rdd = sc.parallelize(list_string)
    count = rdd.count()
    return count

def read_table(table_name):
    from spark import get_spark
    spark_session = get_spark()

    import pandas as pd
    result = spark_session.sql("SELECT * FROM %s"%table_name)
    pandas_df = result.toPandas()
    json_result = pandas_df.to_json(orient='split')
    return json_result
