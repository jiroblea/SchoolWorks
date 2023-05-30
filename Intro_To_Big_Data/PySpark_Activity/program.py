# %% [markdown]
# Data Manipulation Using RDD
# by Junius Iosif Oblea
# 6/30/2023

# %%
import findspark
findspark.init()

# %%
import pyspark
from pyspark import SparkContext

# %%
conf = pyspark.SparkConf().setMaster("local").setAppName("BigData-CarPriceDataset").setAll([("spark.driver.memory", "40g"), ("spark.executor.memory", "50g")])
sc = SparkContext(conf= conf)

# %%
sc.version

# %%
sc.pythonVer

# %%
sc.master

# %%
rdd = sc.textFile("carprice.csv")

# %%
type(rdd)

# %%
rdd.collect()

# %%
rdd.count()

# %%
def doesItInclude(element: list, specification: str):
    """ 
    condition to filter rdd
    """
    if specification in element:
        return element

rdd_filter = rdd.filter(lambda x: doesItInclude(x, 'hatchback') and doesItInclude(x, 'fwd') and doesItInclude(x, 'honda'))
rdd_filter.collect()

# %%
rdd_filter.count()

# %%
rdd_map = rdd.map(lambda x: [x])
rdd_map.collect()

# %%
rdd_flatmap = rdd.flatMap(lambda x: [x.split(',')])
rdd_flatmap.collect()

# %%
rdd_flatmap.count()

# %%
def convertToFloat(element):
    """
    convert the type str to type float if possible
    """
    output = []
    for i in range(len(element)):
        try:
            output.append(float(element[i]))
        except ValueError:
            output.append(element[i])
    return output

# %%
rdd_using_float_type = rdd_flatmap.map(lambda x: convertToFloat(x))
rdd_using_float_type.collect()

# %%
rdd_using_float_type.count()

# %%
header = rdd_using_float_type.first() #extract header
rdd_wo_header = rdd_using_float_type.filter(lambda x: x != header)
rdd_wo_header.collect()

# %%
rdd_wo_header.count()

# %%
rdd_wo_question_mark = rdd_wo_header.filter(lambda x: None if doesItInclude(x, '?') else x)
rdd_wo_question_mark.collect()

# %%
rdd_wo_question_mark.count()

# %%
rdd_filter_price = rdd_wo_question_mark.filter(lambda x: x if float(x[25]) > 15000 else None)
rdd_filter_price.collect()

# %%
rdd_filter_price.count()


