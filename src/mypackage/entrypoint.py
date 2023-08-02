# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/
# https://www.pythontutorial.net/tkinter/ttk-style/
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-theme-layer.html
# https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
# entry point
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

from tkinter.messagebox import showinfo

import os
import pandas as pd

"""
filepath = "raw_data.csv"
#tests
if not os.path.exists(filepath):
  #create it
  print("NOT FOUND DATA")
  mydataset = {
  'name': [],
  'passphrase': [],
  'email': []
  }
  df = pd.DataFrame(mydataset)
  print(df)
  df.to_csv('raw_data.csv', index=False)
  #pass
else:
  df = pd.read_csv('raw_data.csv')
  print(df)
  # Add Row to DataFrame
  #list_row = ['Test', 'Test', 'test@test.test']
  #df.loc[len(df)] = list_row

  #print(df.loc)

  # Insert Dict to the dataframe using DataFrame.append()
  #new_row = {'name':'Test', 'passphrase':'hello', 'email':'test@test.test'}
  #df = df._append(new_row, ignore_index=True)

  df.to_csv('raw_data.csv', index=False)
  print("FOUND DATA")
"""


#class appWindowUI(tk.Tk):
class appWindowUI(ThemedTk):
  def __init__(self):
    super().__init__()
    self.filepath = "raw_data.csv"

    # Adding a title to the window
    self.wm_title("Test Application")
    self.geometry("400x300")
    #self.tk.call('source', 'azure/azure.tcl')

    # Create a style
    style = ttk.Style(self)
    #print("style:", style)
    #style.theme_use('azure')
    #style.theme_use('aquativo')
    #print("themes:", style.theme_names())
    style.theme_use('yaru')

    # label
    self.label = ttk.Label(text="Name")
    self.label.grid(row = 0, column = 0)
    #self.label.pack()

    self.inputName = ttk.Entry()
    self.inputName.grid(row = 0, column = 1)
    #self.inputName.pack()

    self.lpassphrase = ttk.Label(text="Passphrase")
    self.lpassphrase.grid(row = 1, column = 0)
    #self.lpassphrase.pack()

    self.inputPassphrase = ttk.Entry()
    self.inputPassphrase.grid(row = 1, column = 1)
    #self.inputPassphrase.pack()

    self.lemail = ttk.Label(text="E-Mail")
    self.lemail.grid(row = 2, column = 0)
    #self.lemail.pack()

    self.inputEmail = ttk.Entry()
    self.inputEmail.grid(row = 2, column = 1)
    #self.inputEmail.pack()

    # button
    self.button = ttk.Button(self, text='Add')
    self.button['command'] = self.button_clicked
    self.button.grid(row = 3, column = 0, columnspan = 2)
    #self.button.pack()

    #self.progressbar = ttk.Progressbar()
    #self.progressbar.pack()

    #self.spinbox = ttk.Spinbox()
    #self.spinbox.pack()

  def button_clicked(self):
    print("inputPassphrase: ",self.inputPassphrase.get())

    input_name = self.inputName.get()
    input_passphrase = self.inputPassphrase.get()
    input_email = self.inputEmail.get()
    
    #showinfo(title='Information', message='Hello, Tkinter!')
    if not os.path.exists(self.filepath):
      mydataset = {
        'name': [],
        'passphrase': [],
        'email': []
      }
      df = pd.DataFrame(mydataset)
      print(df)
      df.to_csv(self.filepath, index=False)
    else:
      df = pd.read_csv(self.filepath)
      # Insert Dict to the dataframe using DataFrame.append()
      new_row = {'name':input_name, 'passphrase':input_passphrase, 'email':input_email}
      df = df._append(new_row, ignore_index=True)
      df.to_csv('raw_data.csv', index=False)

def run():
  print("Py tkinter!")

  app = appWindowUI()
  app.mainloop()