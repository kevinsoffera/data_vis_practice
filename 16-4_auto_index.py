import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            station_name = row[1]
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    ax.set_title(f"Daily high and low temperatures - 2018\n{station_name}", 
        fontsize = 20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set(ylim = (0, 140))
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()