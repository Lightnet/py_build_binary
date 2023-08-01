# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/
# https://www.pythontutorial.net/tkinter/ttk-style/
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-theme-layer.html
# https://python-course.eu/tkinter/entry-widgets-in-tkinter.php

# entry point
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

from tkinter.messagebox import showinfo

#class appWindowUI(tk.Tk):
class appWindowUI(ThemedTk):
  def __init__(self):
    super().__init__()
    # Adding a title to the window
    self.wm_title("Test Application")
    self.geometry("400x300")
    #self.tk.call('source', 'azure/azure.tcl')

    # Create a style
    style = ttk.Style(self)
    print("style:", style)
    #style.theme_use('azure')
    #style.theme_use('aquativo')
    #print("themes:", style.theme_names())
    style.theme_use('yaru')

    # label
    self.label = ttk.Label(text="Name")
    self.label.pack()

    self.input = ttk.Entry()
    self.input.pack()

    self.lpassphrase = ttk.Label(text="Passphrase")
    self.lpassphrase.pack()

    self.inputPassphrase = ttk.Entry()
    self.inputPassphrase.pack()

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

    #self.progressbar = ttk.Progressbar()
    #self.progressbar.pack()

    #self.spinbox = ttk.Spinbox()
    #self.spinbox.pack()



  def button_clicked(self):
    print("inputPassphrase: ",self.inputPassphrase.get())
    #showinfo(title='Information', message='Hello, Tkinter!')


def run():
  print("Hello World py tkinter!")

  app = appWindowUI()
  app.mainloop()