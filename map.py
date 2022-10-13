class map:
    def __init__(self, *, window, map_pack, root_size, size):
        self.root = window
        self.pack = map_pack
        self.root_size = root_size
        self.size = size
        self.cell_size = root_size[0] / (map_pack.tiles_count * size[0])

        self.scaled_image