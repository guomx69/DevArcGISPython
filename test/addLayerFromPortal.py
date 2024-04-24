from arcgis.gis import GIS

portal=GIS()

trailheads_id = "2e4b3df6ba4b44969a3bc9827de746b3"

trailheads_item = portal.content.get(trailheads_id)
trailheads_item

m = portal.map()
m.add_layer(trailheads_item)
m