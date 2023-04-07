# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

import os, csv
import nltk as nlp
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

with open('sentimentVader.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Year", "Chart", "Negative", "Neutral", "Positive", "Compound"])

with open('genius_Lyrics - Cleanup 1.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	for row in reader:
		#words = nlp.word_tokenize(row[2])
		sid = SentimentIntensityAnalyzer()
		sentiment = sid.polarity_scores(row[3])
		#print(sentiment)
		
		# Save Vader scores to CSV
		with open('sentimentVader.csv', 'a', newline='') as wordsCSVfile:
			write = csv.writer(wordsCSVfile)
			write.writerow([row[1], row[0], sentiment["neg"], sentiment["neu"], sentiment["pos"], sentiment["compound"]])
		
######
###### Graphs
######

# Load CSV and store Vader averages as a dataframe
dfANEW = pd.read_csv('sentimentVader.csv', usecols = ['Year','Negative', "Neutral", "Positive", "Compound"])
print(dfANEW)
dfANEW.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Averages', fontsize=15)
plt.title("Average VADER scores per Year - Song Titles")
plt.show()