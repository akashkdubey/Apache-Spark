'''
Sparkcontext is the entry point for spark environment. For every sparkapp you need to create the sparkcontext object.
Sparkconf is the class which gives you the various option to provide configuration parameters.
'''

conf= SparkConf().setAppName('bm25-hyperparameter-tuning')
sc = SparkContext(conf=conf)
