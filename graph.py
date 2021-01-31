import json
import plotly.graph_objects as go

filename = 'points.json'
with open(filename) as f:
	total_points = json.load(f)

fig = go.Figure()

for player, points in total_points.items():
	fig.add_trace(go.Scatter(y=points, mode='lines+markers',
		name=player.title()))

fig.update_layout(title='Toronto Raptors Playoff Stats', hovermode="x unified",
	xaxis_title='Game', yaxis_title='Points')
fig.show()
