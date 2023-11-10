import pyautogui as ptg
from pynput.mouse import Listener
import tkinter as tk

class Mouse:
    def __init__(self) -> None:
        pass

    class Recorder:
        def __init__(self):
            self.window = tk.Tk()
            self.create_display()

        def create_display(self):
            self.window.title("Mouse Recorder")
            self.window.geometry("300x200")
            self.window.resizable(False, False)

            self.mouse_position = tk.StringVar()
            self.label = tk.Label(self.window, textvariable=self.mouse_position)
            self.label.config(font=("Arial", 12))
            self.label.pack()

            self.hold_mouse_position = tk.StringVar()
            self.holdLabel = tk.Label(self.window, textvariable=self.hold_mouse_position)
            self.holdLabel.config(font=("Arial", 12),bg="Green")
            self.holdLabel.pack()

            self.window.bind("<Control_L>", self.update_hold_mouse_position)
            self.update_mouse_position()

            self.window.mainloop()

        def update_mouse_position(self):
            self.mouse_position.set(f"Current Mouse pos.: x: {ptg.position().x}, y: {ptg.position().y}")
            self.window.after(100, self.update_mouse_position)  # update every 100 ms

        def update_hold_mouse_position(self,event):
            print(event)
            self.hold_mouse_position.set(f"Hold Mouse pos.: x: {ptg.position().x}, y: {ptg.position().y}")

mouse = Mouse()
mouse.Recorder().create_display()