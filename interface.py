import tkinter as tk
from tkinter import *
from adminControlPanel import adminControl
from zoneControlPanel import zoneControl
from tempSensor import tempSensor

running = True
adminPanel = adminControl()
z1 = zoneControl()
zonePanels = []
temp = tempSensor
currentTempint = z1.get_temp()
currentTemp = str(currentTempint)

root = tk.Tk()
def getCurrentTemp():
    currentTempint = z1.get_temp()
    currentTemp = str(currentTempint)
    return currentTemp

    


root.title('Heating and Cooling System Controller')
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure(1, minsize=200, weight=1)

answerWindow = tk.Frame(root)
frameButtons = tk.Frame(root, relief=tk.RAISED, bd=2)

label = tk.Label(text="Heating and Cooling System Controller", fg="black")

setTemp = tk.Button(frameButtons,text="Set Temperature")
setTemp.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

getTemp = tk.Button(frameButtons,text="Get Temperature", command=getCurrentTemp)
getTemp.grid(row=1, column=0, sticky="ew", padx=5)

toggleHeating = tk.Button(frameButtons,text="Toggle Heating")
toggleHeating.grid(row=2, column=0, sticky="ew", padx=5)

toggleCooling = tk.Button(frameButtons,text="Toggle Cooling")
toggleCooling.grid(row=3, column=0, sticky="ew", padx=5)

tutorial = tk.Button(frameButtons,text="How to use")
tutorial.grid(row=4, column=0, sticky="ew", padx=5)

setTempValue = Entry(answerWindow, bg="light yellow")
setTempValue.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

getTempValue = tk.Label(answerWindow, text="Current Temp: " + currentTemp)
getTempValue.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

heatingToggle = tk.Label(answerWindow, text="{Heating : on/off}")
heatingToggle.grid(row=2, column=0, sticky="ew", padx=5)

coolingToggle = tk.Label(answerWindow, text="{Cooling : on/off}")
coolingToggle.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

tutorialText = tk.Label(answerWindow, text="{how to use the controller}")
tutorialText.grid(row=4, column=0, sticky="ew", padx=5)

frameButtons.grid(row=0, column=0, sticky="ns")
answerWindow.grid(row=0, column=1, sticky="nsew")


root.mainloop()
