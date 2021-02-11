import csv
import json

data = {
	'kawhi leonard': {'points': [], 'assists': [], 'rebounds': []},
	'kyle lowry': {'points': [], 'assists': [], 'rebounds': []},
	'pascal siakam': {'points': [], 'assists': [], 'rebounds': []},
	'danny green': {'points': [], 'assists': [], 'rebounds': []},
	'marc gasol': {'points': [], 'assists': [], 'rebounds': []},
}
filenames = [
	'magic_1.csv', 'magic_2.csv', 'magic_3.csv', 'magic_4.csv', 'magic_5.csv',
	'76ers_1.csv', '76ers_2.csv', '76ers_3.csv', '76ers_4.csv', '76ers_5.csv',
	'76ers_6.csv', '76ers_7.csv',
	'bucks_1.csv', 'bucks_2.csv', 'bucks_3.csv', 'bucks_4.csv', 'bucks_5.csv',
	'bucks_6.csv',
	'warriors_1.csv', 'warriors_2.csv', 'warriors_3.csv', 'warriors_4.csv',
	'warriors_5.csv', 'warriors_6.csv',
]

# Collect points, assists, and rebounds data.
for filename in filenames:
	with open('raw_data/' + filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		
		# Find starters.
		for row in reader:
			player = row[0].split('\\')[0].lower()
			if player in data.keys():
				points = int(row[19])
				assists = int(row[14])
				rebounds = int(row[11]) + int(row[12])
				data[player]['points'].append(points)
				data[player]['assists'].append(assists)
				data[player]['rebounds'].append(rebounds)

# Save data.
filename = 'data.json'
with open(filename, 'w') as f:
	json.dump(data, f, indent=4)
