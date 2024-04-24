from arcgis.gis import GIS
#from IPython.display import display
from os import environ
from dotenv import load_dotenv #from .env file
from arcgis.mapping import WebMap

load_dotenv()

print("##############################")
print("ArcGIS Online as anonymous user")    
gis = GIS()
print("Logged in as anonymous user to " + gis.properties.portalName)
public_content = gis.content.search("Fire", item_type="Feature Layer", max_items=5)

for item in public_content:
  print(item.title)

portal = GIS("https://pythonapi.playground.esri.com/portal")
print("Logged in as anonymous user to " + portal.properties.portalName)


print("##############################")
print("pull the information from ArcGIS Online as user", environ.get("user"))


gis = GIS("https://www.arcgis.com", environ.get("user"),environ.get("passwd"))
public_content = gis.content.search("*", item_type="Feature Layer", max_items=5)
for item in public_content:
  print(item.title)
print(f"Connected to {gis.properties.portalHostname} as {gis.users.me.username}")

usa_map = gis.map('USA', zoomlevel=4)  # you can specify the zoom level when creating a map
usa_map
usa_map.basemaps