import os, csv
import nltk as nlp
from nltk.probability import FreqDist
import pandas as pd
import matplotlib.pyplot as plt

hapaxList = []

with open('hapaxList.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Year", "Chart", "Hapax Count", "Hapaxes"])
	
# Iterate through word count/list file
with open('wordCountsNLTK.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	
	for row in reader:
		print(row[0] + " " + row[1])
		tokens = nlp.word_tokenize(row[2])
		fdist = FreqDist(tokens)
		
		#print(fdist.hapaxes())
		
		# Save hapaxes to CSV
		with open('hapaxList.csv', 'a', newline='') as wordsCSVfile:
			write = csv.writer(wordsCSVfile)
			write.writerow([row[0], row[1], len(fdist.hapaxes()), fdist.hapaxes()])
			
# Load CSV and store Vader averages as a dataframe
dfHapax = pd.read_csv('hapaxList.csv', usecols = ['Year','Hapax Count'])
print(dfHapax)
dfHapax.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Averages', fontsize=15)
plt.title("Average Hapax count per Year")
plt.show()