import csv
from datetime import datetime


open_file1 = open("sitka_weather_2018_simple.csv", "r")
csv_file1 = csv.reader(open_file1, delimiter=",")
header_row1 = next(csv_file1)


open_file2 = open("death_valley_2018_simple.csv", "r")
csv_file2 = csv.reader(open_file2, delimiter=",")
header_row2 = next(csv_file2)


for index, column_header in enumerate(header_row1):
    #print("Index:", index, "Column Name:", column_header)
    if column_header == "TMIN":
        tmin1 = index
    if column_header == "TMAX":
        tmax1 = index


highs1 = []
lows1 = []
dates1 = []
name1 = []


for index, column_header in enumerate(header_row2):
    #print("Index:", index, "Column Name:", column_header)
    if column_header == "TMIN":
        tmin2 = index
    if column_header == "TMAX":
        tmax2 = index



highs2 = []
lows2 = []
dates2 = []
name2 = []




for row in csv_file1:
    try:
        high1 = int(row[tmax1])
        low1 = int(row[tmin1])
        converted_date1 = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date1}")
    else:
        highs1.append(int(row[5]))
        lows1.append(int(row[6]))
        name1.append(row[1])
        dates1.append(converted_date1)


for row in csv_file2:
    try:
        high = int(row[tmin2])
        low = int(row[tmax2])
        converted_date2 = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date2}")
    else:
        highs2.append(int(row[4]))
        lows2.append(int(row[5]))
        name2.append(row[1])
        dates2.append(converted_date2)


# plot chart 1
import matplotlib.pyplot as plt


fig, a = plt.subplots(2, sharex= True, sharey= False)

plt.suptitle("Temperature comparison between " + name1[0] + " and " + name2[0])

# chart 1
a[0].set_title(name1[0])
a[0].plot(dates1, highs1, c="red")
a[0].plot(dates1, lows1, c="blue")

a[0].fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)


# chart 2
a[1].set_title(name2[0])
a[1].plot(dates2, highs2, c="red")
a[1].plot(dates2, lows2, c="blue")

a[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)


plt.show()
