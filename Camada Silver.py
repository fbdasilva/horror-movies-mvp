# Databricks notebook source
from pyspark.sql.functions import *

df = spark.table("workspace.default.horror_movies")

print("Registros originais:", df.count())

# Remover colunas que não serão utilizadas
colunas_remover = [
    "tagline",
    "poster_path",
    "runtime",
    "adult",
    "backdrop_path",
    "genre_names",
    "collection",
    "collection_name",
    "overview",
    "original_title",
    "status"
]

df_filtered = df.drop(*colunas_remover)

# Remover linhas que possuem valores nulos nas colunas restantes
df_filtered = df_filtered.dropna()

print("Registros após tratamento:", df_filtered.count())

# Exibir os dados
display(df_filtered)

# Criar a nova tabela
df_filtered.write.mode("overwrite").saveAsTable(
    "workspace.default.horror_movies_processed"
)