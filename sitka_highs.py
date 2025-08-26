from pathlib import Path
from datetime import datetime

# "a", "b", "c", .... 등의 콤마로 구분된 데이터 형식
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')

# splitlines() - 각 행을 리스트로 분리
lines = path.read_text().splitlines()

# 파일의 각 행을 분석할 때 사용할 객체
reader = csv.reader(lines)

# next() - 다음 행으로 진행하기 위해 사용
header_row = next(reader)
# print(header_row)

# 날짜, 최고, 최저 기온 추출
dates, highs, lows = [], [], []
for row in reader:
    # strptime() - 문자열을 날짜로 해석
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# print(highs)

# 추출한 최고, 최저 기온 그래프화
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(12, 8), dpi=200)

# alpha 인수를 통해 투명도 설정 (0 to 1)
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)

# fill_between() 메서드를 사용하여 그래프의 사이를 채움
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 그래프 형식
ax.set_title('Daily High and Low Temperature, 2021', fontsize=14)
ax.set_xlabel('', fontsize=12)

# 날짜는 yyyy-mm-dd 형식으로 길기에 대각선으로 표시
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=12)
ax.tick_params(labelsize=12)

plt.show()

# enumerate() - 리스트를 순회하며 항목의 인덱스와 값을 반환
# for index, column_head in enumerate(header_row):
#     print(index, column_head)