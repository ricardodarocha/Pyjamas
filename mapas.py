import pandas as pd
import folium
import webbrowser

guidoval = folium.Map(
    location=[-21.151944, -42.796944],    # Coordenadas retiradas do Google Maps
    zoom_start=18
)

folium.Marker([-21.151744,-42.798159], ['Casa do Ricardo']).add_to(guidoval)

guidoval.save('opa.html') 
url = 'opa.html'
webbrowser.open(url,new=2)
#mais info https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Colormaps.ipynb