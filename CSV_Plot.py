import csv
import re

import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

file_name = 'sitka_weather_07-2014.csv'

# 分析CSV文件头
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# 打印文件头及其位置
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, header_row in enumerate(header_row):
        print(index, header_row)

# 打印(第一行)最高温所有值

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, max_temps, mean_temps = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        max_temp = int(row[1])
        max_temps.append(max_temp)
        mean_temp = int(row[2])
        mean_temps.append(mean_temp)

plt.plot(dates,max_temps)
plt.plot(dates,mean_temps)
# 着色呈现每天的气温范围
plt.fill_between(dates, max_temps, mean_temps, facecolor='blue', alpha=0.1)

# with open(filename) as file:
#     for row in reader:
#         try:
#             current_date = datetime.strptime(row[0], "%Y-%m-%d")
#             high = int (row[0])
#             low = int (row(3))
#         except:
#             print(current_date, 'Error')


def get_character_number(filename):
    count =0
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for i in row:
                with open("工作簿1.txt", 'a', encoding='utf-8') as f:
                    f.write(i + " ")

get_character_number(file_name)


result = pd.read_csv(file_name)
print(result)
print("Number of lines present:-",
      len(result))

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
x = re.findall("Portugal", txt)
x = re.search("\s", txt)
print(x.start())