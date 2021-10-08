import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get Data
    brights, lons, lats = [], [], []
    for row in reader:
        brights.append(row[2])
        lons.append(row[1])
        lats.append(row[0])

# Map the fires.
data = [{
'type': 'scattergeo',
'lon': lons,
'lat': lats,
'marker': {
    'size': [0.02*float(bright) for bright in brights],
    'color': [0.02*float(bright) for bright in brights],
    'colorscale': 'hot',
    'colorbar': {'title': 'Brightness'},
    }
}]

my_layout = Layout(title='Global Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')