# https://pypi.org/project/py-readability-metrics/#dale-chall-readability
# https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula

import os, csv
import nltk as nlp
from readability import Readability
import pandas as pd
import matplotlib.pyplot as plt

with open('lexicalReadability.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Year", "Chart", "Dale Chall Score", "Dale Chall Grade Levels"])
	
# Iterate through word count/list file
with open('genius_Lyrics - Cleanup 1.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	
	for row in reader:
		try:
			print(row[0] + " " + row[1])
			r = Readability(row[4])
			dc = r.dale_chall()
			
			# Save Dale Chall readability scores to CSV
			with open('lexicalReadability.csv', 'a', newline='') as wordsCSVfile:
				write = csv.writer(wordsCSVfile)
				write.writerow([row[1], row[0], dc.score, dc.grade_levels])
		except:
			print(row[0] + " " + row[1])
			# Save Dale Chall readability scores to CSV
			with open('lexicalReadability.csv', 'a', newline='') as wordsCSVfile:
				write = csv.writer(wordsCSVfile)
				write.writerow([row[1], row[0], 0, 0])
		
# Load CSV and store DaleChall averages as a dataframe
dfDCScore = pd.read_csv('lexicalReadability.csv', usecols = ['Year','Dale Chall Score'])
print(dfDCScore)
dfDCScore.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Averages', fontsize=15)
plt.title("Average Dale Chall Score per Year")
plt.show()