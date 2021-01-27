#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:23:33 2021

@author: Mason Barnes
"""

import os
import platform
import flask
import webbrowser
from datetime import datetime
app = flask.Flask(__name__)

def average(lst):
    return round(sum(lst)/len(lst), 2)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/")
def home():
    try:
        weekly_data_high = []
        weekly_data_low = []
        with open("data.txt", "r") as f:
            file_chunks = f.read().split("\n")
            if len(file_chunks) <= 7:
                for line in file_chunks:
                    data_info = line.split(", ")
                    weekly_data_high.append(int(data_info[0]))
                    weekly_data_low.append(int(data_info[1]))
            else:
                for line in file_chunks[:-7]:
                    data_info = line.split(", ")
                    weekly_data_high.append(int(data_info[0]))
                    weekly_data_low.append(int(data_info[1]))
        data1 = "Average Weekly High: " + str(average(weekly_data_high))
        data2 = "Average Weekly Low: " + str(average(weekly_data_low))
    except:
        data1 = "Average Weekly High: NOT AVAILABLE"
        data2 = "Average Weekly Low: NOT AVAILABLE"
    try:
        all_time_data_high = []
        all_time_data_low = []
        with open("data.txt", "r") as f:
            file_chunks = f.read().split("\n")
            for line in file_chunks:
                data_info = line.split(", ")
                all_time_data_high.append(int(data_info[0]))
                all_time_data_low.append(int(data_info[1]))
        data3 = "Average All Time High: " + str(average(all_time_data_high))
        data4 = "Average All Time Low: " + str(average(all_time_data_low))
    except:
        data3 = "Average All Time High: NOT AVAILABLE"
        data4 = "Average All Time Low: NOT AVAILABLE"
    with open("web/index.html") as f: return f.read().replace("DATA1", data1).replace("DATA2", data2).replace("DATA3", data3).replace("DATA4", data4)

@app.route("/add-data", methods=['GET'])
def add_data():
    now = datetime.now()
    blood_high = int(flask.request.args.get("high"))
    blood_low = int(flask.request.args.get("low"))
    if flask.request.args.get("date") == "null" or flask.request.args.get("date") == "" or flask.request.args.get("date") == None:
        date = now.strftime("%m/%d/%Y")
        date = date[:-4]+date[-2:]
    else:
        try:
            date = flask.request.args.get("date")
            datetime.strptime(date[:6]+"20"+date[-2:], '%m/%d/%Y')
        except:
            return "Invalid date!"
    replaced = False
    with open("data.txt", "r") as f:
        file_data = f.read().split("\n")
        try:
            file_data.remove('')
        except:
            pass
        for line in file_data:
            if date in line:
                file_data[file_data.index(line)] = "{}, {}, {}".format(blood_high, blood_low, date)
                replaced = True
    if not replaced:
        file_data.append("{}, {}, {}".format(blood_high, blood_low, date))
    file_data = sorted(file_data, key=lambda x: datetime.strptime(x.split(", ")[2][:6]+"20"+x.split(", ")[2][-2:], '%m/%d/%Y'))
    with open("data.txt", "w") as f:
        f.write("\n".join(file_data))
    return '<script>alert("Data successfully added. Press \\"OK\\" to return."); window.location.replace("http://localhost:7634");</script>'

@app.route("/weekly-plot")
def display_weekly_plot():
    if platform.system() == "Windows":
        os.system("python3 weekly_chart.py")
    elif platform.system() == "Darwin":
        os.system("sudo python3 weekly_chart.py")
    return flask.send_file('weekly_chart.png')

@app.route("/all-time-plot")
def display_all_time_plot():
    os.system("python3 all_time_chart.py")
    return flask.send_file('all_time_chart.png')

# This is a placeholder, please ignore this
app.run(host="localhost", port=7634)
