import matplotlib.pyplot as plt
from shutil import copyfile

try:
    weekly_data_high = []
    weekly_data_low = []
    dates = []
    with open("data.txt", "r") as f:
        file_chunks = f.read().split("\n")
        if len(file_chunks) <= 7:
            for line in file_chunks:
                data_info = line.split(", ")
                weekly_data_high.append(int(data_info[0]))
                weekly_data_low.append(int(data_info[1]))
                dates.append(data_info[2])
        else:
            for line in file_chunks[:-7]:
                data_info = line.split(", ")
                weekly_data_high.append(int(data_info[0]))
                weekly_data_low.append(int(data_info[1]))
                dates.append(data_info[2])
    plt.figure()
    plt.plot(dates, weekly_data_high, dates, weekly_data_low)

    plt.xlabel("Date")
    plt.ylabel("Blood Pressure")
    plt.title("Weekly Data (Blue = High, Orange = Low)")

    plt.savefig('weekly_chart.png')
except:
    copyfile("no_data.png", "weekly_chart.png")