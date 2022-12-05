import tkinter as tk
from tkinter import *
from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl

adminPanel = AdminControl()
zonePanel = ZoneControl()
root = tk.Tk()

root.title('Heating and Cooling System Controller')
root.minsize(300, 200)


def get_power_usage():
    return zonePanel.get_power_consumed()


def get_money_spent():
    return get_power_usage() * zonePanel.get_cost_per_kwh()


def get_money_saved():
    return 50


power_usage = tk.Label(text="Power usage (Kwh): %i" % get_power_usage())
power_usage.pack()

money_spent = tk.Label(text="Money Spent (Euro): %.2f" % get_money_spent())
money_spent.pack()

money_saved = tk.Label(text="Money Saved (Euro): %i" % get_money_saved())
money_saved.pack()

root.mainloop()
