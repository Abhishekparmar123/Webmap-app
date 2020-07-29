import folium
import pandas
import io


def color_producer(elevation):
    if elevation < 1000:
        return 'green'

    elif 1000 <= elevation < 3000:
        return 'orange'

    else:
        return 'red'


data = pandas.read_csv("Volcanoes.txt")
data_json = io.open('world.json', 'r', encoding='utf-8-sig').read()
lan = list(data["LAN"])
lat = list(data["LAT"])

map = folium.Map(location=[39.9352, -43.9453], zoom_start=2, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
elev = list(data["ELEV"])

for lt, ln, el in zip(lat, lan, elev):
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln], popup=str(el) + " m", radius=10, color='gray',
                            fill_color=color_producer(el), fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': '#ffeb3b' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LatLngPopup())
map.add_child(folium.LayerControl())

map.save("Map1.html")
