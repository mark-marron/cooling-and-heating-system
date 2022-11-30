import tkinter as tk
from tkinter import *
from adminControlPanel import AdminControl

adminPanel = AdminControl()
root = tk.Tk()

root.title('Statistics')
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure(1, minsize=200, weight=1)

root.mainloop()