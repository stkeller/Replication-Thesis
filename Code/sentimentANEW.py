import os, csv
import nltk as nlp
import pandas as pd
import matplotlib.pyplot as plt


# Create ANEW dictionary
anew = {}
with open('anewList.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	for row in reader:
		# 0 = Word// 1 = Valence// 2 = Arousal// 3 = Dominance// 4 = Happiness// 5 = Anger// 6 = Sadness// 7 = Fear// 8 = Disgust
		anew[row[0]] = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],]


with open('sentimentANEW.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Year", "Chart", "ANEW Words Count",
						"Valence Total", "Valence Average", "Arousal Total", "Arousal Average", "Dominance Total", "Dominance Average",
						"Happiness Total", "Happiness Average", "Anger Total", "Anger Average", "Sadness Total", "Sadness Average",
						"Fear Total", "Fear Average", "Disgust Total", "Disgust Average"])

		
# Iterate through word count/list file
with open('wordCountsNLTK.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	for row in reader:
		wordCounter = 1
		valence, arousal, dominance = 0,0,0
		happiness, anger, sadness, fear, disgust = 0,0,0,0,0
		
		words = nlp.word_tokenize(row[2])
		for word in words:
			if anew.get(word) != None:
				wordCounter = wordCounter + 1
				valence += float(anew.get(word)[0])
				arousal += float(anew.get(word)[1])
				dominance += float(anew.get(word)[2])
				happiness += float(anew.get(word)[3])
				anger += float(anew.get(word)[4])
				sadness += float(anew.get(word)[5])
				fear += float(anew.get(word)[6])
				disgust += float(anew.get(word)[7])
			if wordCounter == 0:
				wordCounter = 1
		
		# Save values to CSV
		with open('sentimentANEW.csv', 'a', newline='') as wordsCSVfile:
			write = csv.writer(wordsCSVfile)
			write.writerow([row[0], row[1], wordCounter,
								valence, valence/wordCounter, arousal, arousal/wordCounter, dominance, dominance/wordCounter,
								happiness,happiness/wordCounter, anger,anger/wordCounter, sadness,sadness/wordCounter,
								fear,fear/wordCounter, disgust,disgust/wordCounter])

		
######
###### Graphs
######

# Load CSV and store ANEW averages as a dataframe
dfANEW = pd.read_csv('sentimentANEW.csv', usecols = ['Year','Valence Average', "Arousal Average", "Dominance Average"])
print(dfANEW)
dfANEW.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Averages', fontsize=15)
plt.title("Average ANEW values per Year")
plt.show()

# Load CSV and store ANEW emotion averages as a dataframe
dfEmotion = pd.read_csv('sentimentANEW.csv', usecols = ['Year','Happiness Average', "Anger Average", "Sadness Average",
														"Fear Average", "Disgust Average"])
print(dfEmotion)
dfEmotion.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Averages', fontsize=15)
plt.title("Average ANEW Emotion values per Year")
plt.show()