from arcgis.gis import GIS

portal=GIS()

trailheads_id = "2e4b3df6ba4b44969a3bc9827de746b3"

trailheads_item = portal.content.get(trailheads_id)
trailheads_item

m = portal.map()
m.add_layer(trailheads_item)
m

m.center = [34.09042, -118.71511]  # [latitude, longitude]
m.zoom = 11