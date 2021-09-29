import plotly.express as px
from plotly import offline

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.

while True:

    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    fig = px.scatter(x=rw.x_values, y=rw.y_values)

    # Emphasize the first and last points.
    

    # Remove the axes.
    

    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break