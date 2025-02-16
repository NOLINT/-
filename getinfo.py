import requests

# Overpass API URL
url = "http://overpass-api.de/api/interpreter"

# クエリ（横須賀市安浦町近くのベンチと飲食店を取得）
query = """
[out:json];
(
  node["amenity"="bench"](35.28, 139.66, 35.29, 139.67);
  node["amenity"="restaurant"](35.28, 139.66, 35.29, 139.67);
);
out body;
"""

response = requests.get(url, params={'data': query})
data = response.json()

# 結果を表示
for element in data['elements']:
    print(element['tags'].get('name', 'Unnamed'), element['lat'], element['lon'])
