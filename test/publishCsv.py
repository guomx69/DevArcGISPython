from IPython.display import display
from arcgis.gis import GIS
import os
gis = GIS("https://www.arcgis.com", environ.get("user"),environ.get("passwd"))
data = "/home/mint/projects/test/DevGISModels/QGIS/projects/Data/Data.zip"
shpfile = gis.content.add({}, data)
shpfile

ming_folder_details = gis.content.create_folder('ming')
print(ming_folder_details)

published_service = shpfile.publish()
display(published_service)