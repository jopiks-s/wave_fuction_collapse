from packet import packet
from tkinter import *
from PIL import Image, ImageTk


class map:
    def __init__(self, *, window: Tk, tiles_packet: packet, window_size, map_size):
        self.root = window
        self.tiles_packet = tiles_packet
        self.root_size = window.winfo_height()
        self.size = map_size
        self.cell_size = (int(window_size[0] / (map_size[0])), int(window_size[1] / (map_size[1])))

        tiles_packet.tiles = {name: img.resize(self.cell_size) for name, img in tiles_packet.tiles.items()}
        for x in range(map_size[0]):
            for y in range(map_size[1]):
                l = Label(image=tiles_packet.tiles["down"])
                l.place(x=x * self.cell_size[0], y=y * self.cell_size[1])
