from arcgis.gis import GIS
#from IPython.display import display
from os import environ
from dotenv import load_dotenv #from .env file
from arcgis.mapping import WebMap

load_dotenv()

gis = GIS("https://www.arcgis.com", environ.get("user"),environ.get("passwd"))
print(f"Connected to {gis.properties.portalHostname} as {gis.users.me.username}")

usa_map = gis.map('USA', zoomlevel=4)  # you can specify the zoom level when creating a map
usa_map

world_timezones_item = gis.content.get('312cebfea2624e108e234220b04460b8')
usa_map.add_layer(world_timezones_item)
world_countries_item = gis.content.get('ac80670eb213440ea5899bbf92a04998')
world_countries_layer = world_countries_item.layers[0]
world_countries_layer
usa_map.add_layer(world_countries_layer, options={'opacity':0.4})

webmap_properties = {'title':'USA time zones and traffic counts WebMap',
                    'snippet': 'Jupyter notebook widget saved as a web map',
                    'tags':['automation', 'python']}

webmap_item = usa_map.save(webmap_properties)