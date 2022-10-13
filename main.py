from tkinter import *
from PIL import Image, ImageTk
from packet import *
from map import *
import image


def ini_window(w, h):
    window = Tk()
    x = int(window.winfo_screenwidth() / 2 - w / 2)
    y = int(window.winfo_screenheight() / 2 - h / 2)
    window.geometry(f"{w}x{h}+{x}+{y}")
    return window


w, h = 700, 700

window = ini_window(w, h)
tiles_packet = packet("road")
map = map(window=window, tiles_packet=tiles_packet, window_size=(w, h), map_size=(10, 10))


def main():
    pass
    # window.mainloop()


if __name__ == '__main__':
    main()
