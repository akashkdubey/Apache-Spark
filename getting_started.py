'''
Sparkcontext is the entry point for spark environment. For every sparkapp you need to create the sparkcontext object.
Sparkconf is the class which gives you the various option to provide configuration parameters. The spark configuration 
is passed to spark context.You can also set different application configuration in sparkconf and pass to sparkcontex
'''
import pyspark
from pyspark import SparkContext, SparkConf

conf= SparkConf().setAppName('hello-test')
sc = SparkContext(conf=conf)
