import geopandas as gpd

parks=gpd.read_file("/home/mint/projects/test/DevGISModels/QGIS/projects/Data/houston.shp")
parks.plot()
