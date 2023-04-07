# https://pypi.org/project/py-readability-metrics/#dale-chall-readability
# https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula

import os, csv
from random import sample
import nltk as nlp
import pandas as pd
import matplotlib.pyplot as plt

sampleSize = 6000
sampleTimes = 20
years = []
TTR = []

# Iterate through word count/list file
with open('genius_LyricsCombined.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	
	for row in reader:
		TTRSampled =[]
		for i in range(sampleTimes):
			tokens = nlp.word_tokenize(row[1])
			tokensSample = sample(tokens,sampleSize)
			types = nlp.Counter(tokensSample)
			TTRSampled.append(len(types)/len(tokensSample)*100)
		
		years.append(row[0])
		TTR.append(sum(TTRSampled)/sampleTimes)

print(years)
print(TTR)		
		
# Store values into PD dataframe and plot average word count values
dfTTR = pd.DataFrame({"Year": years, "TTR": TTR})
print(dfTTR)
dfTTR.plot("Year")
plt.xlabel('Year', fontsize=15)
plt.ylabel('TTR', fontsize=15)
plt.title("Sampled Type Token Ratio per year")
plt.show()