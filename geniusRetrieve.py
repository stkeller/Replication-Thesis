import lyricsgenius
import csv

genius = lyricsgenius.Genius("YOSi5j-Us3Le1D4xOiLmqux4Ux_UEkzGqrR3IrBdlUztitYsd8U3w9mj5UEu-lNz")

with open('genius_Lyrics.csv', 'w', newline='') as AZLyricsCSV:
		write = csv.writer(AZLyricsCSV)
		write.writerow(["Chart", "Year", "Artist", "Song", "Lyrics"])

with open('songList.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		try:
			song = genius.search_song(row[2], row[3])
			
			print(row[0] + " " + row[1])
			lyricsFile = open(row[1] + "_" + row[0] + ".txt", "w")
			lyricsFile.write(song.lyrics)
			with open('genius_Lyrics.csv', 'a', newline='') as AZLyricsCSV:
				write = csv.writer(AZLyricsCSV)
				write.writerow([row[0], row[1], row[3], row[2], song.lyrics])
		except:
			print("Error:" + " " + row[0] + " " + row[1])
			lyricsFile = open(row[1] + "_" + row[0] + ".txt", "w")
			lyricsFile.write("n/a")
			with open('genius_Lyrics.csv', 'a', newline='') as AZLyricsCSV:
				write = csv.writer(AZLyricsCSV)
				write.writerow([row[0], row[1], row[3], row[2], "N/A"])