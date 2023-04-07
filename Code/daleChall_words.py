# Dale-Chall list retrieved from: https://gist.github.com/Abhishek-P/e00edcc6f508640fe24f263f5836a7dc
import os, csv
import nltk
import nltk as nlp
import pandas as pd
from collections import Counter

daleChall = open("daleChallList.txt").read()
daleChall_tokens = nltk.word_tokenize(daleChall)
ignoreList = ["i", "'", "'", "," ,"!", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "instrumental"]

# Create csv files
with open('nonDaleChallWords.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Chart", "Year", "Non_Dale_Chall_Words"])
with open('nonDaleChallWords_counts.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Year", "Non_Dale_Chall_Words_COUNTS"])

with open('genius_Lyrics.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	for row in reader:
		daleChall_NotinLyrics = []
		lyrics = row[4]
		lyrics = lyrics.lower()
		lyrics_tokens = nltk.word_tokenize(lyrics)
		# check if words in lyrics are not in the dale-chall list
		for token in lyrics_tokens:
			if token not in daleChall_tokens and token not in ignoreList:
				daleChall_NotinLyrics.append(token)
		#print(daleChall_NotinLyrics)
		# save words to csv file
		with open('nonDaleChallWords.csv', 'a', newline='', encoding='utf-8') as wordsCSVfile:
			write = csv.writer(wordsCSVfile)
			separator = " "
			write.writerow([row[0], row[1], separator.join(daleChall_NotinLyrics)])

# Group words by year
df = pd.read_csv('nonDaleChallWords.csv', usecols = ['Year', 'Non_Dale_Chall_Words'])
df = df.groupby(["Year"]).agg(list)
df.to_csv("nonDaleChallWords.csv", encoding='utf-8')

# Store word counts into CSV file
with open('nonDaleChallWords.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	for row in reader:
		words = nlp.word_tokenize(row[1])
		wordCounts = nlp.Counter(words)
		with open('nonDaleChallWords_counts.csv', 'a', newline='') as wordsCSVfile:
			write = csv.writer(wordsCSVfile)
			write.writerow([row[0], wordCounts])