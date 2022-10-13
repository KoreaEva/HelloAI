import folium

map = folium.Map(location=[37,127],zoom_start=7)

marker = folium.Marker([37.341435483, 126.733026596],
                    popup='한국공학대학교', 
                    icon = folium.Icon(color='blue'))

marker.add_to(map) 

map.save(r'27. 전국의 대학교 위치 시각화하기/uni_map.html')