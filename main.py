from tkinter import *
from PIL import Image, ImageTk
from packet import *

w, h = 800, 700
road_pack = packet("road")


def main():
    pass


if __name__ == '__main__':
    main()


def window():
    root = Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    w_x = int(sw / 2 - w / 2)
    w_y = int(sh / 2 - h / 2)
    root.geometry(f"{w}x{h}+{w_x}+{w_y}")
    root.mainloop()
