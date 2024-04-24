from arcgis.gis import GIS
from arcgis.geocoding import geocode

from os import environ

gis = GIS(url="https://www.arcgis.com", username=environ.get("user"),password=environ.get("passwd"))
geocode_result = geocode(address="21823 barton park ln, katy tx 77450")
print(geocode_result)  #need print, but in Jupyter notebook no need print.

