import json
import plotly.graph_objects as go

# Data
filename = 'data.json'
with open(filename) as f:
	data = json.load(f)
games = [
	'Magic Game 1', 'Magic Game 2', 'Magic Game 3', 'Magic Game 4',
	'Magic Game 5',
	'76ers Game 1', '76ers Game 2', '76ers Game 3', '76ers Game 4',
	'76ers Game 5', '76ers Game 6', '76ers Game 7',
	'Bucks Game 1', 'Bucks Game 2', 'Bucks Game 3', 'Bucks Game 4',
	'Bucks Game 5', 'Bucks Game 6',
	'Warriors Game 1', 'Warriors Game 2', 'Warriors Game 3',
	'Warriors Game 4', 'Warriors Game 5', 'Warriors Game 6',
]
colors = {
	'kawhi leonard': 'rgb(206, 17, 65)',
	'kyle lowry': 'rgb(6, 25, 34)',
	'pascal siakam': 'rgb(161, 161, 164)',
	'danny green': 'rgb(180, 151, 90)',
	'marc gasol': 'rgb(117, 59, 189)',
}

# Plot
fig = go.Figure()
for player in data:
	fig.add_trace(
		go.Scatter(
			x=games,
			y=data[player]['points'],
			mode='lines+markers',
			name=player.title(),
			line=dict(color=colors[player], width=4),
			marker=dict(size=6),
		)
	)

# Add buttons to view points, assists, and rebounds.
fig.update_layout(
	updatemenus=[
		dict(
			type='buttons',
			direction='down',
			showactive=True,
			buttons=list([
				dict(
					label="Points",
					method="update",
					args=[{"y":[
						data['kawhi leonard']['points'],
						data['kyle lowry']['points'],
						data['pascal siakam']['points'],
						data['danny green']['points'],
						data['marc gasol']['points'],
					]}],
				),
				dict(
					label="Assists",
					method="update",
					args=[{"y":[
						data['kawhi leonard']['assists'],
						data['kyle lowry']['assists'],
						data['pascal siakam']['assists'],
						data['danny green']['assists'],
						data['marc gasol']['assists'],
					]}],
				),
				dict(
					label="Rebounds",
					method="update",
					args=[{"y":[
						data['kawhi leonard']['rebounds'],
						data['kyle lowry']['rebounds'],
						data['pascal siakam']['rebounds'],
						data['danny green']['rebounds'],
						data['marc gasol']['rebounds'],
					]}],
				),
			]),
		)
	]
)

# Update titles and hovermode.
fig.update_layout(
	title=dict(text='Toronto Raptors 2019 Playoffs', font_size=30),
	xaxis_title=dict(text='Game', font_size=20),
	yaxis_title=dict(text='Total', font_size=20),
	hovermode="x unified",
	template='seaborn',
)

fig.show()
