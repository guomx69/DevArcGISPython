from arcgis.gis import GIS

gis = GIS("https://www.arcgis.com")
usa_map = gis.map('USA', zoomlevel=4)  # you can specify the zoom level when creating a map
usa_map.basemaps
