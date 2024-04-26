#https://developers.arcgis.com/python/guide/introduction-to-the-spatially-enabled-dataframe/
#https://www.youtube.com/watch?v=h1Lnz-rfWQo
from arcgis import GIS
import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
gis = GIS()
item = gis.content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
flayer = item.layers[0]

# create a Spatially Enabled DataFrame object
sdf = pd.DataFrame.spatial.from_layer(flayer)
sdf.head()