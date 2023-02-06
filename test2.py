#Reading a csv file using pyspark

from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master["local[*]"].appName("git").getOrCreate()



data = "C:\\Bigdata\\driver\\emp.csv"

df = spark.read.format('csv').option("header","true").load(data)

df.show()
