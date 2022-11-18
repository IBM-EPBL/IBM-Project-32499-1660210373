import datetime as dt
import time
import board
import busio
from anyleaf import PhSensor, OnBoard

LOOP_DELAY = 60 * 5  # Time to sleep, in seconds.
LOG_FILENAME = "ph_readings.csv"


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    ph_sensor = PhSensor(i2c, LOOP_DELAY)

    while True:
        ph = ph_sensor.read(OnBoard())
        timestamp = dt.datetime.now()

        # Open our log file in append-line mode. This way new lines can be 
        # written without overwriting existing ones.
        with open(LOG_FILENAME, 'a') as f:
            # Write the timestamp to the first column, and pH to the second.
            f.write(f"{timestamp.isoformat()},{round(ph, 2)}\n")

        # Wait for 5 minutes before taking and logging another reading.
        time.sleep(LOOP_DELAY)


if __name__ == "__main__":
    main()
