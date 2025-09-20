import os
import csv
from datetime import datetime

FILE_NAME = "data.csv"

def main():
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)

        # If file is absent, create with header
        if not file_exists:
            writer.writerow(["timestamp"])

        # Append new row with current timestamp
        writer.writerow([datetime.now().isoformat()])

if __name__ == "__main__":
    main()
