from packet import packet
from tkinter import Tk
class map:
    def __init__(self, *, window: Tk, tiles_packet: packet, window_size, map_size):
        self.root = window
        self.tiles_packet = tiles_packet
        self.root_size = window.winfo_height()
        self.size = map_size
        print(type(self.root_size))
        print(self.root_size)
        self.cell_size = window_size[0] / (tiles_packet.tiles_count * map_size[0])

        #self.scaled_image