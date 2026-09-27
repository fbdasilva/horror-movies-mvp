# Databricks notebook source
# MAGIC %md
# MAGIC ## 1. Ranqueamento da performance dos filmes.

# COMMAND ----------

# MAGIC %md
# MAGIC ### a) Quais os 10 filmes mais populares?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT title, popularity FROM horror_movies_processed ORDER BY popularity DESC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### b) Quais os 5 filmes mais bem avaliados?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT title, vote_average FROM horror_movies_processed ORDER BY vote_average DESC LIMIT 5;

# COMMAND ----------

# MAGIC %md
# MAGIC ### c) Quais são os 5 filmes com maior orçamento?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT title, budget FROM horror_movies_processed ORDER BY budget DESC LIMIT 5;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Evolução do desempenho dos filmes.

# COMMAND ----------

# MAGIC %md
# MAGIC ### a) Qual a quantidade de filmes por década?

# COMMAND ----------

from pyspark.sql.functions import *

# Ler a tabela tratada
df = spark.table("horror_movies_processed")

# Contar quantidade de filmes por década
df_movies_decade = (
    df
    .withColumn("year", year("release_date"))
    .withColumn("decade", (col("year") / 10).cast("int") * 10)
    .groupBy("decade")
    .agg(
        count("*").alias("number_of_movies")
    )
    .orderBy("decade")
)

# Exibir resultado
display(df_movies_decade)

# COMMAND ----------

# MAGIC %md
# MAGIC ### b) Como foi a evolução do orçamento médio por década?

# COMMAND ----------

from pyspark.sql.functions import *

df = spark.table("horror_movies_processed")

df_budget = (
    df
    .filter(col("budget") > 0)
    .withColumn("year", year("release_date"))
    .withColumn("decade", (col("year") / 10).cast("int") * 10)
    .groupBy("decade")
    .agg(
        avg("budget").alias("average_budget"),
        count("*").alias("number_of_movies_filtered")
    )
    .orderBy("decade")
)

display(df_budget)

# COMMAND ----------

# MAGIC %md
# MAGIC ### c) Como foi a evolução da receita média por década?

# COMMAND ----------

from pyspark.sql.functions import *

df = spark.table("horror_movies_processed")

df_revenue = (
    df
    .filter(col("revenue") > 0)
    .withColumn("year", year("release_date"))
    .withColumn("decade", (col("year") / 10).cast("int") * 10)
    .groupBy("decade")
    .agg(
        avg("revenue").alias("average_revenue"),
        count("*").alias("number_of_movies_filtered")
    )
    .orderBy("decade")
)

display(df_revenue)