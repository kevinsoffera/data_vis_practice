import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high and low temmperatures from this file.
    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        precipitation = float(row[3])
        dates.append(current_date)
        precipitations.append(precipitation)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, precipitations, c='blue', alpha=0.5)

    # Format plot
    ax.set_title("Daily precipitation - 2018", fontsize = 24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Precipitation (Inches)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()