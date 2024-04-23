from arcgis import GIS

portal=GIS()

webmap_search = portal.content.search(
  query="LA Parks and Trails Map (styled) tags:tutorial owner:esri_devlabs",
  item_type="Web Map"
)
webmap_search

webmap_item = webmap_search[0]
webmap_item

from arcgis.mapping import WebMap
la_park_trails = WebMap(webmap_item)
la_park_trails