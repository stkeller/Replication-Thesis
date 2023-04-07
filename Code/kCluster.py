import os, csv
import nltk as nlp
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('wordCountsNLTK.csv', usecols = ['Year','Chart', "Word count", "Unique Word Count"])
df1 = df[['Word count', 'Unique Word Count']]

kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit(df1)
df['Cluster'] = clusters.labels_.tolist()
df.to_csv("kCluster.csv")

plt.scatter(df["Word count"], df["Unique Word Count"], s=1, c=kmeans.labels_)
plt.show()