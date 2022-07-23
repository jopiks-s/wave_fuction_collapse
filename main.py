from tkinter import *
from PIL import Image, ImageTk
from packet import *
from map import *
import image

w, h = 700, 700

window = Tk()
map_pack = packet("road")
map = map(window=window, map_pack=map_pack, root_size=(w, h), size=(10, 10))


def main():
    pass

# sw = window.winfo_screenwidth()
# sh = window.winfo_screenheight()
# w_x = int(sw / 2 - w / 2)
# w_y = int(sh / 2 - h / 2)
# window.geometry(f"{w}x{h}+{w_x}+{w_y}")
# window.mainloop()


if __name__ == '__main__':
    main()
