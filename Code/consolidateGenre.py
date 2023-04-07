import os, csv
import nltk as nlp
import pandas as pd

genre = []
originalGenre = []
year = []
chart = []
artist = []
song = []
with open('consolidatedGenres.csv', 'w', newline='') as wordsCSVfile:
				write = csv.writer(wordsCSVfile)
				write.writerow(["Year", "Chart", "Artist", "Song", "Genre", "Original Genre"])


# Iterate through word count/list file
with open('k3_4_5_Cluster.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	next(reader)
		
	for row in reader:
		year.append(row[0])
		chart.append(row[1])
		artist.append(row[2])
		song.append(row[3])
		originalGenre.append(row[4])
	
		if "surf" in row[4]:
			genre.append("surf")
		elif "rock" in row[4]:
			genre.append("rock")
		elif "metal" in row[4]:
			genre.append("rock")
		elif "disco" in row[4]:
			genre.append("disco")
		elif "funk" in row[4]:
			genre.append("funk")
		elif "adult standards" in row[4]:
			genre.append("adult standards")
		elif "adult standard" in row[4]:
			genre.append("adult standards")
		elif "easy listening" in row[4]:
			genre.append("adult standards")
		elif "nashville sound" in row[4]:
			genre.append("adult standards")
			
		
		elif "r&b" in row[4]:
			genre.append("r&b")
		elif "rhythm and blues" in row[4]:
			genre.append("r&b")
		elif "doo-wop" in row[4]:
			genre.append("r&b")
		elif "doo wop" in row[4]:
			genre.append("r&b")
		elif "jazz" in row[4]:
			genre.append("jazz")
		elif "blues" in row[4]:
			genre.append("blues")
		elif "motown" in row[4]:
			genre.append("r&b")
		elif "soul" in row[4]:
			genre.append("soul")
		elif "country" in row[4]:
			genre.append("country")
		elif "western" in row[4]:
			genre.append("country")
		elif "reggae" in row[4]:
			genre.append("reggae")
		
		elif "hip hop" in row[4]:
			genre.append("hip hop")
		elif "rap" in row[4]:
			genre.append("hip hop")
		
		elif "pop" in row[4]:
			genre.append("pop")
		elif "britpop" in row[4]:
			genre.append("pop")
		elif "house" in row[4]:
			genre.append("dance")
		elif "dance" in row[4]:
			genre.append("dance")
		elif "edm" in row[4]:
			genre.append("dance")
			
		elif "mexicana" in row[4]:
			genre.append("latin")
		elif "reggaeton" in row[4]:
			genre.append("latin")
		elif "tropical" in row[4]:
			genre.append("latin")
		
		else:
			genre.append("N/A")
print(len(genre))



for i in range(len(genre)):
	with open('consolidatedGenres.csv', 'a', newline='') as wordsCSVfile:
				write = csv.writer(wordsCSVfile)
				write.writerow([year[i], chart[i], song[i], artist[i], genre[i], originalGenre[i]])