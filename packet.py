from xml.dom import minidom
from definitions import *
from PIL import Image
import xml.etree.ElementTree as ET
import numpy as np
import os


class packet:
    maps_folder = f"{ROOT_DIR}/maps/"

    def __init__(self, map_name):
        self.map_name = map_name
        self.map_folder = packet.maps_folder + map_name + '/'

        if not os.path.isdir(self.map_folder):
            print(c_colors.FAIL + "can't find map dir at: " + self.map_folder)
            print(c_colors.FAIL + "map doesn't exist")
            return
        if not os.path.isfile(self.map_folder + map_name + ".xml"):
            print(c_colors.FAIL + "can't find xml rules at: " + self.map_folder + map_name + ".xml")
            print(c_colors.FAIL + "xml rules doesn't exist, to create use packet.craete_map(...)")
            return

        self.tiles = []
        for file in os.listdir(self.map_folder):
            if file.split('.')[1] in ("png", "jpg"):
                self.tiles.append(Image.open(self.map_folder+file))


def create_map(map_name, tiles_count):
    root = minidom.Document()

    packet = root.createElement(map_name)
    root.appendChild(packet)

    for i in range(tiles_count):
        item = root.createElement(f"tile{i}")
        rules = root.createElement("rules")
        item.appendChild(rules)
        packet.appendChild(item)
        for dir in ["UP", "LEFT", "DOWN", "RIGHT"]:
            rule = root.createElement(dir)
            rule.setAttribute("sockets", str([0] * tiles_count))
            rules.appendChild(rule)

    xml_str = root.toprettyxml(indent="\t")

    map_dir = f"{ROOT_DIR}/maps/{map_name}"
    file_name = f"{map_dir}/{map_name}.xml"

    if not os.path.isdir(map_dir):
        os.mkdir(map_dir)

    elif os.path.isfile(file_name):
        rewrite = input("xml map already exist, rewrite? y/n?: ")
        if rewrite == "n":
            return

    with open(file_name, "w") as f:
        f.write(xml_str)

    print(f"{map_name} created")
