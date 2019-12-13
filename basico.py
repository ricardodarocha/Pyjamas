#Tutorial 
import json
import pandas as pd
import requests
import webbrowser
import folium

# 1. estas url ser„o usadas para pegar a geometria e os dados do MAPA
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
us_states = f'{url}/us-states.json'
US_Unemployment_Oct2012 = f'{url}/US_Unemployment_Oct2012.csv'

geo_json_data = json.loads(requests.get(us_states).text)  
unemployment = pd.read_csv(US_Unemployment_Oct2012)
unemployment_dict = unemployment.set_index('State')['Unemployment']

# 2. FunÁ„o para calcular a cor do elemento
def my_color_function(feature):
    """Maps low values to green and high values to red."""
    if unemployment_dict[feature['id']] > 6.5:
        return '#ff0000' #vermelho
    else:
        return '#008000' #verde

# 3. cria um mapa, posicionando em uma coordenada geogr√°fica                          
guidoval = folium.Map(
    location=[-21.151944, -42.796944],    # Coordenadas retiradas do Google Maps
    zoom_start=18,
    control_scale = True,
    tiles='OpenStreetMap',
    attr="<a href=https://endless-sky.github.io/>Endless Sky</a>"
)

# 4. Aplica a formatacao ao gr·fico                       
folium.GeoJson(
    geo_json_data,
    style_function=lambda feature: {
        'fillColor': my_color_function(feature),
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5'
    }
).add_to(guidoval)            
                           
url = 'opa.html'
guidoval.save(url) 
webbrowser.open(url,new=2)              