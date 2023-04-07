import os, csv
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV and store genres and clusters into dataframe. Remove entries with no genre
dfCLusters = pd.read_csv('kCluster_and_Genre.csv', usecols = ["Genre", "Cluster k5"])
dfCLusters[dfCLusters["Genre"].str.contains("N/A")==False]

# Split each cluster into new dataframe
dfCluster_0 = dfCLusters[dfCLusters['Cluster k5'] == 0]
dfCluster_1 = dfCLusters[dfCLusters['Cluster k5'] == 1]
dfCluster_2 = dfCLusters[dfCLusters['Cluster k5'] == 2]
dfCluster_3 = dfCLusters[dfCLusters['Cluster k5'] == 3]
dfCluster_4 = dfCLusters[dfCLusters['Cluster k5'] == 4]
# count genres in each cluster
dfCLusters_0_counts = dfCluster_0.pivot_table(index = ['Genre'], aggfunc ='size')
dfCLusters_1_counts = dfCluster_1.pivot_table(index = ['Genre'], aggfunc ='size')
dfCLusters_2_counts = dfCluster_2.pivot_table(index = ['Genre'], aggfunc ='size')
dfCLusters_3_counts = dfCluster_3.pivot_table(index = ['Genre'], aggfunc ='size')
dfCLusters_4_counts = dfCluster_4.pivot_table(index = ['Genre'], aggfunc ='size')
# print hip-hop counts for each cluster
print("0 = " + str(dfCLusters_0_counts["hip hop"]))
print("1 = " + str(dfCLusters_1_counts["hip hop"]))
print("2 = " + str(dfCLusters_2_counts["hip hop"]))
print("3 = " + str(dfCLusters_3_counts["hip hop"]))
print("4 = " + str(dfCLusters_4_counts["hip hop"]))

"""
# Pie chart for hip hop on cluster 0
labels = 'hip hop', 'other genres'
counts = [dfCLusters_0_counts["hip hop"], len(dfCluster_0.index) - dfCLusters_0_counts["hip hop"]]
fig, ax = plt.subplots()
ax.pie(counts, labels=labels)
plt.title("Cluster 0")
plt.show()
# Pie chart for hip hop on cluster 1
labels = 'hip hop', 'other genres'
counts = [dfCLusters_0_counts["hip hop"], len(dfCluster_1.index) - dfCLusters_1_counts["hip hop"]]
fig, ax = plt.subplots()
ax.pie(counts, labels=labels)
plt.title("Cluster 1")
plt.show()
# Pie chart for hip hop on cluster 2
labels = 'hip hop', 'other genres'
counts = [dfCLusters_0_counts["hip hop"], len(dfCluster_2.index) - dfCLusters_2_counts["hip hop"]]
fig, ax = plt.subplots()
ax.pie(counts, labels=labels)
plt.title("Cluster 2")
plt.show()
# Pie chart for hip hop on cluster 3
labels = 'hip hop', 'other genres'
counts = [dfCLusters_0_counts["hip hop"], len(dfCluster_3.index) - dfCLusters_3_counts["hip hop"]]
fig, ax = plt.subplots()
ax.pie(counts, labels=labels)
plt.title("Cluster 3")
plt.show()
# Pie chart for hip hop on cluster 4
labels = 'hip hop', 'other genres'
counts = [dfCLusters_0_counts["hip hop"], len(dfCluster_4.index) - dfCLusters_4_counts["hip hop"]]
fig, ax = plt.subplots()
ax.pie(counts, labels=labels)
plt.title("Cluster 4")
plt.show()
"""