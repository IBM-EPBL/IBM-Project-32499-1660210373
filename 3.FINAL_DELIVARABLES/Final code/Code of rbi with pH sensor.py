import csv
import datetime as dt
import matplotlib.pyplot as plt


LOG_FILENAME = "ph_readings.csv"


def main():
    """Plot readings over time, from a CSV log file."""
    timestamps = []
    readings = []
    with open(LOG_FILENAME) as f:
        reader = csv.reader(f)
        for (timestamp, ph) in reader:
            # Parse the timestamp into a `datetime.datetime`.
            timestamps.append(dt.datetime.fromisoformat(timestamp))
            readings.append(float(ph))

    fig, ax = plt.subplots()

    ax.plot(timestamps, readings)  # Use `ax.scatter(...)` for a scatterplot.

    ax.set_title("pH over time")
    ax.set_xlabel('Date and time of reading')
    ax.set_ylabel('pH')
    ax.set_ylim(6, 8)

    plt.show()
