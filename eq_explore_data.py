from pathlib import Path
import json

import plotly.express as px

# 데이터를 문자열로 읽어 python 객체로 변환
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 데이터 파일을 읽기 쉬운 형태로 변경
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# 데이터 집합의 지진 데이터 읽기
all_eq_dicts = all_eq_data['features']

# 지진의 규모, 경도, 위도를 담을 리스트
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = 'Global Earthquakes'

# scatter_geo() - 지도 위에 산포도를 표시하는 메서드
fig = px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()

# 테스트
# print(mags[:10])
# print(lons[:5])
# print(lats[:5])