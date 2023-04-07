import os, csv
from random import sample
import nltk as nlp
import pandas as pd
import matplotlib.pyplot as plt

sampleSize = 200
sampleTimes = 50
TTR = []
years =[]

# Iterate through word count/list file
with open('wordCountsNLTK.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	
	for row in reader:
		tokens = nlp.word_tokenize(row[2])
		TTRSampled =[]
		
		print(row[0] + " " + row[1] + " " + "Population: " + str(len(tokens)))
		
		if len(tokens) > sampleSize:
			for i in range(sampleTimes):
				tokensSample = sample(tokens,sampleSize)
				types = nlp.Counter(tokensSample)
				TTRSampled.append(len(types)/len(tokensSample)*100)
			years.append(row[0])
			TTR.append(sum(TTRSampled)/sampleTimes)
		else:
			pass
	
		
# Store values into PD dataframe and plot average word count values
dfTTR = pd.DataFrame({"Year": years, "TTR": TTR})
print(dfTTR)
dfTTR.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('TTR', fontsize=15)
plt.ylim([30, 90])
plt.title("Sampled Type Token Ratio per year")
plt.show()