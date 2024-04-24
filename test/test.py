from arcgis.gis import GIS

gis = GIS("https://www.arcgis.com")
usa_map = gis.map('USA', zoomlevel=4)  # you can specify the zoom level when creating a map
print(usa_map.basemaps) #need print, but in Jupyter notebook  just usa_map.basemaps

