import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='Mapbox Bright')
fg_v = folium.FeatureGroup(name="Volcanoes")

for lt, lon, el in zip(lat,lon,elev):
	if el < 1000:
		color = 'green'
	elif 1000 <= el < 3000:	
		color = 'orange'
	else:
		color = 'red'
	fg_v.add_child(folium.CircleMarker(location=[lt, lon],popup="Elevation: {0} m".format(el),radius=6, fill_color=color, color="grey",fill_opacity = 0.7))

fg_p = folium.FeatureGroup(name="Population")

fg_p.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig'),style_function = lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())
map.save("Map1.html")