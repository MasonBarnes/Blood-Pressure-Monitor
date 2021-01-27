import matplotlib.pyplot as plt
from shutil import copyfile

try:
    all_time_data_high = []
    all_time_data_low = []
    dates = []
    with open("data.txt", "r") as f:
        file_chunks = f.read().split("\n")
        for line in file_chunks:
            data_info = line.split(", ")
            all_time_data_high.append(int(data_info[0]))
            all_time_data_low.append(int(data_info[1]))
            dates.append(data_info[2])
    plt.figure()
    plt.plot(dates, all_time_data_high, dates, all_time_data_low)

    plt.xlabel("Date")
    plt.ylabel("Blood Pressure")
    plt.title("All Time Data (Blue = High, Orange = Low)")

    plt.savefig('all_time_chart.png')
except:
    copyfile("no_data.png", "all_time_chart.png")