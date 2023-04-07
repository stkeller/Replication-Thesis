#https://www.tandfonline.com/doi/abs/10.1080/09296171003643098

# Covington, Michael & McFall, Joe. Cutting the Gordian Knot: The Moving-Average Type–Token Ratio (MATTR). Journal of Quantitative Linguistics, issue 2, vol 17, 2010

import os, csv
from random import sample
import nltk as nlp
import pandas as pd
import matplotlib.pyplot as plt

window_size = 100
MATTR = []
years =[]

# Iterate through word count/list file
with open('wordCountsNLTK.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
	
	for row in reader:	
		tokens = nlp.word_tokenize(row[2])

		last_index = len(tokens) - window_size
		windowTTR = []
		
		if len(tokens) > window_size:
			for start in range (last_index):
				windowTokens = tokens[start:start+window_size]
				types = nlp.Counter(windowTokens)
				windowTTR.append(len(types)/len(tokens)*100)
			MATTR.append(sum(windowTTR)/len(windowTTR))
			years.append(row[0])
		else:
			pass

# Store values into PD dataframe and plot average word count values
dfMATTR = pd.DataFrame({"Year": years, "MATTR": MATTR})
print(dfMATTR)
dfMATTR.groupby(["Year"]).mean().plot()
plt.xlabel('Year', fontsize=15)
plt.ylabel('MATTR', fontsize=15)
plt.ylim([0, 90])
plt.title("Average Moving Average Type Token Ratio per year")
plt.show()