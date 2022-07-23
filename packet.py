from xml.dom import minidom
from PIL.Image import Image
from definitions import *
from PIL import Image
import xml.etree.ElementTree as ET
import numpy as np
import os


class packet:
    tiles: list[Image]
    maps_folder = f"{ROOT_DIR}/maps/"

    def __init__(self, map_name):
        self.map_name = map_name
        self.map_folder = packet.maps_folder + map_name + '/'
        self.rules_path = self.map_folder + self.map_name + ".xml"
        self.rules = [[{}]]
        self.tiles = {}
        self.tiles_count = 0

        xml = ET.parse(self.rules_path)
        map_root = xml.getroot()

        if not os.path.isdir(self.map_folder):
            print(c_colors.FAIL + "can't find map dir at: " + self.map_folder)
            print(c_colors.FAIL + "map doesn't exist")
            return
        if not os.path.isfile(self.map_folder + map_name + ".xml"):
            print(c_colors.FAIL + "can't find xml rules at: " + self.map_folder + map_name + ".xml")
            print(c_colors.FAIL + "xml rules doesn't exist, to create use packet.craete_map(...)")
            return

        # load images
        for file in os.listdir(self.map_folder):
            if file.split('.')[1] in ("png", "jpg"):
                self.tiles[file.split('.')[0]] = Image.open(self.map_folder + file)

        self.tiles_count = len(self.tiles)
        self.rules = [[{}] * 4 for _ in range(self.tiles_count)]

        if len(map_root) != self.tiles_count:
            print(c_colors.FAIL +
                  f"Corrupted rules file! Folder tiles count: {self.tiles_count}, Rules tile count: {len(map_root)}")
            return

        # load rules
        tiles_mapping = list(self.tiles.keys())
        for i, tile in enumerate(map_root):
            mapped_index = tiles_mapping.index(tile.tag)
            for j, dir_rules in enumerate(tile[0]):
                sockets = dir_rules.attrib["sockets"].strip("[]").split(", ")
                self.rules[mapped_index][j] = {dir_rules.tag: sockets}


def create_map(map_name, tiles_count):
    map_dir = f"{ROOT_DIR}/maps/{map_name}"
    file_name = f"{map_dir}/{map_name}.xml"
    tile_names = []

    if not os.path.isdir(map_dir):
        os.mkdir(map_dir)
        tile_names = [f"tile{tile}" for tile in range(tiles_count)]
    else:
        if os.path.isfile(file_name):
            if input("xml map already exist, rewrite? y/n?: ") == "n":
                return
        print(f"rewriting {file_name}...")
        tile_names = [file.split('.')[0] for file in os.listdir(map_dir) if file.split('.')[1] in ("png", "jpg")]

    root = minidom.Document()

    packet = root.createElement(map_name)
    root.appendChild(packet)

    for i in range(tiles_count):
        item = root.createElement(tile_names[i])
        rules = root.createElement("rules")
        item.appendChild(rules)
        packet.appendChild(item)
        for dir in ["UP", "LEFT", "DOWN", "RIGHT"]:
            rule = root.createElement(dir)
            rule.setAttribute("sockets", str([-1] * tiles_count))
            rules.appendChild(rule)

    xml_str = root.toprettyxml(indent="\t")

    with open(file_name, "w") as f:
        f.write(xml_str)

    print(f"{map_name} created")
