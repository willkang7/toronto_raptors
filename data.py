import csv
import json

total_points = {
	'kawhi leonard': [],
	'kyle lowry': [],
	'pascal siakam': [],
	'danny green': [],
	'marc gasol': [],
	}
total_assists = {
	'kawhi leonard': [],
	'kyle lowry': [],
	'pascal siakam': [],
	'danny green': [],
	'marc gasol': [],
	}
total_rebounds = {
	'kawhi leonard': [],
	'kyle lowry': [],
	'pascal siakam': [],
	'danny green': [],
	'marc gasol': [],
	}
filenames = [
	'magic_1.csv', 'magic_2.csv', 'magic_3.csv', 'magic_4.csv', 'magic_5.csv',
	'76ers_1.csv', '76ers_2.csv', '76ers_3.csv', '76ers_4.csv', '76ers_5.csv', '76ers_6.csv', '76ers_7.csv',
	'bucks_1.csv', 'bucks_2.csv', 'bucks_3.csv', 'bucks_4.csv', 'bucks_5.csv', 'bucks_6.csv',
	'warriors_1.csv', 'warriors_2.csv', 'warriors_3.csv', 'warriors_4.csv', 'warriors_5.csv', 'warriors_6.csv']

# Find data.
for filename in filenames:
	with open('data/' + filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		
		for row in reader:
			player = row[0].split('\\')[0].lower()
			if player in total_points.keys():
				points = int(row[19])
				assists = int(row[14])
				rebounds = int(row[11]) + int(row[12])
				total_points[player].append(points)
				total_assists[player].append(assists)
				total_rebounds[player].append(rebounds)

# Save data.
filename = 'data/points.json'
with open(filename, 'w') as f:
	json.dump(total_points, f, indent=4)
filename = 'data/assists.json'
with open(filename, 'w') as f:
	json.dump(total_assists, f, indent=4)
filename = 'data/rebounds.json'
with open(filename, 'w') as f:
	json.dump(total_rebounds, f, indent=4)
