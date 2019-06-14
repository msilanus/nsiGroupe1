import csv

data = []

title = True
csvfile = open("history_export_2019-06-10T17_44_15.csv")

for line in csv.reader(csvfile,csv.Sniffer().sniff(csvfile.read(1024))):
    data.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]), float(line[5]), float(line[6])])
open("data_wind.js", "w").write('raw_data = ' + str(data))

print(data)