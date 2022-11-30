import tkinter as tk
from tkinter import *
from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl

adminPanel = AdminControl()
root = tk.Tk()

root.title('Heating and Cooling System Controller')
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure(1, minsize=200, weight=1)
answerWindow = tk.Frame(root)
frameButtons = tk.Frame(root, relief=tk.RAISED, bd=2)
label = tk.Label(text="Heating and Cooling System Controller", fg="black")

def get_power_usage():
    return 50

def get_money_spent():
    return 100

def get_money_saved():
    return 150

root.mainloop()