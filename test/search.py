from arcgis.gis import GIS
from IPython.display import display
# from os import environ
# from dotenv import load_dotenv #from .env file
# load_dotenv()


print("ArcGIS Online as anonymous user")    
gis = GIS()
print("Logged in as anonymous user to " + gis.properties.portalName)
public_content = gis.content.search("Fire", item_type="Feature Layer", max_items=5)

for item in public_content:
  display(item)