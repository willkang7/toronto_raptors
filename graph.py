import json
import plotly.graph_objects as go

# Get data.
filename = 'data/points.json'
with open(filename) as f:
	total_points = json.load(f)
filename = 'data/assists.json'
with open(filename) as f:
	total_assists = json.load(f)
filename = 'data/rebounds.json'
with open(filename) as f:
	total_rebounds = json.load(f)

# Create graph.
fig = go.Figure()

for player, points in total_points.items():
	fig.add_trace(
		go.Scatter(
			y=points,
			mode='lines+markers',
			name=player.title(),
		),
	)

# Add buttons for graphs of points, assists, and rebounds.
fig.update_layout(
	updatemenus=[
		dict(
			type="buttons",
			direction="right",
			x=0.7,
			y=1.2,
			showactive=True,
			buttons=list(
				[
					dict(
						label="Points",
						method="update",
						args=[{"y":[
							total_points['kawhi leonard'],
							total_points['kyle lowry'],
							total_points['pascal siakam'],
							total_points['danny green'],
							total_points['marc gasol'],
						]}],
					),
					dict(
						label="Assists",
						method="update",
						args=[{"y":[
							total_assists['kawhi leonard'],
							total_assists['kyle lowry'],
							total_assists['pascal siakam'],
							total_assists['danny green'],
							total_assists['marc gasol'],
						]}],
					),
					dict(
						label="Rebounds",
						method="update",
						args=[{"y":[
							total_rebounds['kawhi leonard'],
							total_rebounds['kyle lowry'],
							total_rebounds['pascal siakam'],
							total_rebounds['danny green'],
							total_rebounds['marc gasol'],
						]}],
					),
				]
			),
		)
	]
)

# Update titles and hovermode.
fig.update_layout(
	title='Toronto Raptors Playoffs Stats',
	hovermode="x unified",
	xaxis_title='Game',
	yaxis_title='Total',
)

fig.show()
