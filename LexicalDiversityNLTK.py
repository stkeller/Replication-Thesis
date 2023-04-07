#https://pythonexamples.org/python-find-unique-words-in-text-file/
#https://www.pythonpool.com/python-loop-through-files-in-directory/

import os, csv
import pandas as pd
import matplotlib.pyplot as plt
import nltk as nlp
from nltk.corpus import stopwords

wordCount = []
wordCount_noStopwords = []
uniqueWordCount = []
uniqueWordCount_noStopwords = []
typeTokenRatio = []
typeTokenRatio_noStopwords = []

storeYear = []
storeChart = []

songLength = []
words_perSecond = []
UniqueWords_perSecond = []
TTR_perSecond = []

with open('wordCountsNLTK.csv', 'w', newline='') as wordsCSVfile:
		write = csv.writer(wordsCSVfile)
		write.writerow(["Year", "Chart", "Words", "Unique words", "Words - no stopwords", "Unique words - no stopwords",
						"Word count", "Unique Word Count", "Type Token Ratio",
						"Word count - no Stopwords", "Unique Word Count - no Stopwords", "Type Token Ratio - no Stopwords",
						"Words per second", "Unique words per second", "TTR per second",
						"Words per second - no Stopwords", "Unique words per second - no Stopwords", "TTR per second - no Stopwords"])


#Iterate through lyrics csv file
with open('genius_Lyrics.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	for i, row in enumerate(reader):
		lyrics = row[4]
		print(i)
		
		# Tokenize
		lyrics = lyrics.lower()
		tokens = nlp.word_tokenize(lyrics)
		types = nlp.Counter(tokens)
		
		# Remove stopwords
		tokens_noStopwords = [word for word in tokens if not word in stopwords.words()]
		types_noStopwords = nlp.Counter(tokens_noStopwords)
		
		# Append file name, year, chart and word counts to lists
		storeYear.append(row[1])
		storeChart.append(row[0])
		
		wordCount.append(len(tokens))
		wordCount_noStopwords.append(len(tokens_noStopwords))
		uniqueWordCount.append(len(types))
		uniqueWordCount_noStopwords.append(len(types_noStopwords))
		typeTokenRatio.append(len(types)/len(tokens)*100)
		if len(types_noStopwords) > 0 and len(tokens_noStopwords) > 0:
			typeTokenRatio_noStopwords.append(len(types_noStopwords)/len(tokens_noStopwords)*100)
		else:
			typeTokenRatio_noStopwords.append(0)
		
		songLength.append(float(row[5]))
		words_perSecond = [value/songLength[index] for index,value in enumerate(wordCount)]
		words_perSecond_noStopwords = [value/songLength[index] for index,value in enumerate(wordCount_noStopwords)]
		UniqueWords_perSecond = [value/songLength[index] for index,value in enumerate(uniqueWordCount)]
		UniqueWords_perSecond_noStopwords = [value/songLength[index] for index,value in enumerate(uniqueWordCount_noStopwords)]
		TTR_perSecond = [value/songLength[index] for index,value in enumerate(typeTokenRatio)]
		TTR_perSecond_noStopwords = [value/songLength[index] for index,value in enumerate(typeTokenRatio_noStopwords)]
		
		#Store values to CSV file
		with open('wordCountsNLTK.csv', 'a', newline='') as wordsCSVfile:
			write = csv.writer(wordsCSVfile)
			write.writerow([storeYear[i], storeChart[i], tokens, types, tokens_noStopwords, types_noStopwords,
							wordCount[i], uniqueWordCount[i], typeTokenRatio[i],
							wordCount_noStopwords[i], uniqueWordCount_noStopwords[i], typeTokenRatio_noStopwords[i],
							words_perSecond[i], UniqueWords_perSecond[i], TTR_perSecond[i],
							words_perSecond_noStopwords[i], UniqueWords_perSecond_noStopwords[i], TTR_perSecond_noStopwords[i]])


######
###### Graphs
######

# Store values into PD dataframe and plot average word count values
dfWords = pd.DataFrame({"Year": storeYear, 
				   "Chart": storeChart,
				   "Word count": wordCount,
				   "Unique Word count": uniqueWordCount})
print(dfWords)
#dfWords['Word count'] = dfWords['Word count'].clip(upper=400)
dfWords.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('word count', fontsize=15)
plt.title("Average unique words and words count per Year")
plt.show()

# Store values into PD dataframe and plot average TTR values
dfTTR = pd.DataFrame({"Year": storeYear, 
				   "Chart": storeChart,
				   "Type Token Ratio": typeTokenRatio})
print(dfTTR)
dfTTR.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Type Token Ratio', fontsize=15)
plt.ylim([0, 100])
plt.title("Average Type Token Ratio per Year")
plt.show()

# Store values into PD dataframe and plot average word per second values
dfWords_perSecond = pd.DataFrame({"Year": storeYear, 
				   "Chart": storeChart,
				   "Words per second": words_perSecond,
				   "Unique words per second": UniqueWords_perSecond,
				   "TTR per second": TTR_perSecond})
print(dfWords_perSecond)
dfWords_perSecond['Words per second'] = dfWords_perSecond['Words per second'].clip(upper=100)
dfWords_perSecond['Unique words per second'] = dfWords_perSecond['Unique words per second'].clip(upper=100)
dfWords_perSecond.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Words per second', fontsize=15)
plt.title("Average words per second per Year")
plt.show()

######
###### Graphs without stopwords
######

# Store values into PD dataframe and plot average word count values
dfWords_noStopwords = pd.DataFrame({"Year": storeYear, 
				   "Chart": storeChart,
				   "Word count": wordCount_noStopwords,
				   "Unique Word count": uniqueWordCount_noStopwords})
print(dfWords_noStopwords)
#dfWords['Word count'] = dfWords['Word count'].clip(upper=400)
dfWords_noStopwords.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('word count', fontsize=15)
plt.title("Average unique words and words count per Year - no stopwords")
plt.show()

# Store values into PD dataframe and plot average TTR values
dfTTR_noStopwords = pd.DataFrame({"Year": storeYear, 
				   "Chart": storeChart,
				   "Type Token Ratio": typeTokenRatio_noStopwords})
print(dfTTR)
dfTTR_noStopwords.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Type Token Ratio', fontsize=15)
plt.ylim([0, 100])
plt.title("Average Type Token Ratio per Year - no stopwords")
plt.show()

# Store values into PD dataframe and plot average word per second values
dfWords_perSecond_noStopwords = pd.DataFrame({"Year": storeYear, 
				   "Chart": storeChart,
				   "Words per second": words_perSecond_noStopwords,
				   "Unique words per second": UniqueWords_perSecond_noStopwords,
				   "TTR per second": TTR_perSecond_noStopwords})
print(dfWords_perSecond_noStopwords)
dfWords_perSecond_noStopwords['Words per second'] = dfWords_perSecond_noStopwords['Words per second'].clip(upper=100)
dfWords_perSecond_noStopwords['Unique words per second'] = dfWords_perSecond_noStopwords['Unique words per second'].clip(upper=100)
dfWords_perSecond_noStopwords.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('Words per second', fontsize=15)
plt.title("Average words per second per Year - no stopwords")
plt.show()