from pathlib import Path
from datetime import datetime

import csv
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 날짜, 최고, 최저 기온 추출
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    # 데이터 누락에 대비해 try, except 사용
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 그래프 형식
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(12, 8), dpi=200)

# alpha 인수를 통해 투명도 설정 (0 to 1)
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)

# fill_between() 메서드를 사용하여 그래프의 사이를 채움
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily High and Low Temperatures, 2021 : Death Valley"
ax.set_title(title, fontsize=14)
ax.set_xlabel('', fontsize=12)

# 날짜는 yyyy-mm-dd 형식으로 길기에 대각선으로 표시
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=12)
ax.tick_params(labelsize=12)

plt.show()

# 데이터 확인용
# for index, column in enumerate(header_row):
#     print(index, column)