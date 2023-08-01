# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/


# entry point
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class appWindowUI(tk.Tk):
  def __init__(self):
    super().__init__()
    # Adding a title to the window
    self.wm_title("Test Application")

    # label
    self.label = ttk.Label(text="Name")
    self.label.pack()

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

def run():
  print("Hello World py tkinter!")

  app = appWindowUI()
  app.mainloop()