import json
import plotly.graph_objects as go

# Get data.
filename = 'data.json'
with open(filename) as f:
	data = json.load(f)

# Plot graph of points.
fig = go.Figure()
for player in data:
	fig.add_trace(
		go.Scatter(
			y=data[player]['points'],
			mode='lines+markers',
			name=player.title(),
		)
	)

# Add buttons to view points, assists, and rebounds.
fig.update_layout(
	updatemenus=[
		dict(
			type='buttons',
			direction='right',
			x=0.7,
			y=1.2,
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
	title='Toronto Raptors Playoffs Stats',
	hovermode="x unified",
	xaxis_title='Game Number',
	yaxis_title='Total',
)

fig.show()
