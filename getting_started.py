'''
Sparkcontext is the entry point for spark environment. For every sparkapp you need to create the sparkcontext object.
Sparkconf is the class which gives you the various option to provide configuration parameters. The spark configuration 
is passed to spark context.You can also set different application configuration in sparkconf and pass to sparkcontex
'''
import pyspark
from pyspark import SparkContext, SparkConf #Sparkcontext is the entry point for spark environment
from pyspark.sql import SparkSession # Main entry point for DataFrame and SQL functionality.


conf= SparkConf().setAppName('hello-test').  # setAppName(value) − To set an application name [most commonly used attributes of SparkConf]
sc = SparkContext(conf=conf)

'''

'''

spark = SparkSession(sc).builder.master("yarn").config("spark.default.parallelism", 6000) \. 
        .config("spark.driver.memory", "32G") \
        .config('spark.executor.memory', '32g') \
        .config('spark.executor.cores', '8') \
        .config('spark.cores.max', '32') \
        .config('spark.yarn.executor.memoryOverhead', '32g') \
        .config('spark.executor.instances', '100') \
        .config('spark.sql.shuffle.partitions', 6) \
        .config("spark.sql.crossJoin.enabled", "true") \
        .config("spark.sql.caseSensitive", "true") \
        .config('spark.sql.autoBroadcastJoinThreshold',-1)\
        .config('spark.sql.broadcastTimeout',3000).getOrCreate()
