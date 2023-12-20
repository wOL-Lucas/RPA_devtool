import pyautogui
import tkinter as tk

def screen_fill(x,y,height, width):
    screen_size = pyautogui.size()
    window = tk.Tk()

    window.geometry(f"{screen_size[0]}x{screen_size[1]}")
    window.attributes("-alpha", 0.3)

    canvas = tk.Canvas(window, width=width, height=height, bd=0, highlightthickness=0, bg = "red")
    canvas.place(x=x,y=y)

    window.mainloop()