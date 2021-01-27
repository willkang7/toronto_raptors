import csv

from plotly.graph_objs import Bar, Layout
from plotly import offline

total_points = {
	'kawhi': [],
	'kyle': [],
	'pascal': [],
	'danny': [],
	'marc': [],
	'fred': [],
	'serge': [],
	'norman': [],
	'jodie': [],
	'patrick': [],
	'jeremy': [],
	'malcolm': [],
	'eric': [],
	'chris': [],
	'og': [],
	'team': [],
	}

filenames = [
	'magic_1.csv', 'magic_2.csv', 'magic_3.csv', 'magic_4.csv', 'magic_5.csv',
	'76ers_1.csv', '76ers_2.csv', '76ers_3.csv', '76ers_4.csv', '76ers_5.csv', '76ers_6.csv', '76ers_7.csv',
	'bucks_1.csv', 'bucks_2.csv', 'bucks_3.csv', 'bucks_4.csv', 'bucks_5.csv', 'bucks_6.csv',
	'warriors_1.csv', 'warriors_2.csv', 'warriors_3.csv', 'warriors_4.csv', 'warriors_5.csv', 'warriors_6.csv']

for filename in filenames:
	with open('data/' + filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		# Get each player's points from this file.
		for row in reader:
			try:
				points = int(row[19])
			except ValueError:
				points = 'DNP'
			player = row[0].split()[0].lower()
			total_points[player].append(points)

print(total_points)
