from arcgis.gis import GIS

from arcgis.geometry import Point,Polygon,Polyline

portal =GIS()

point = Point({"x": -118.8066, "y": 34.0006, "z": 100})

point_attributes = {"name": "Point", "description": "I am a point"}

simple_marker_symbol = {
    "type": "esriSMS",
    "style": "esriSMSCircle",
    "color": [0, 0, 0],
    "outline": {"color": [255, 255, 255], "width": 1},
}


polyline = Polyline(
    {
        "paths": [
            [-118.821527826096, 34.0139576938577],
            [-118.814893761649, 34.0080602407843],
            [-118.808878330345, 34.0016642996246],
        ]
    }
)

polyline_attributes = {"name": "Polyline", "description": "I am a Polyline"}

simple_line_symbol = {
    "type": "esriSLS",
    "style": "esriSLSolid",
    "color": [255, 155, 128],
    "width": 2,
}

polygon = Polygon(
    {
        "rings": [
            [
                [-118.818984489994, 34.0137559967283],
                [-118.806796597377, 34.0215816298725],
                [-118.791432890735, 34.0163883241613],
                [-118.79596686535, 34.008564864635],
                [-118.808558110679, 34.0035027131376],
            ]
        ]
    }
)

polygon_attributes = {"name": "Polygon", "description": "I am a Polygon"}

simple_fill_symbol = {
    "type": "esriSFS",
    "color": [50, 100, 200, 125],
    "outline": {"color": [255, 255, 255], "width": 1},
}

map=portal.map()
map

map.draw(
    shape=point,
    symbol=simple_marker_symbol,
    attributes=point_attributes,
    popup={
        "title": point_attributes["name"],
        "content": point_attributes["description"],
    },
)

map.draw(
    shape=polyline,
    symbol=simple_line_symbol,
    attributes=polyline_attributes,
    popup={
        "title": polyline_attributes["name"],
        "content": polyline_attributes["description"],
    },
)

map.draw(
    shape=polygon,
    symbol=simple_fill_symbol,
    attributes=polygon_attributes,
    popup={
        "title": polygon_attributes["name"],
        "content": polygon_attributes["description"],
    },
)

map.center = [34.0110, -118.8047]
map.zoom = 14

import os

file_dir = os.path.join(os.getcwd(), "home")
if not os.path.isdir(file_dir):
    os.mkdir(file_dir)

file_path = os.path.join(file_dir, "add-a-point-line-and-polygon.html")

map.export_to_html(file_path, title="Add a point, line, and polygon")
