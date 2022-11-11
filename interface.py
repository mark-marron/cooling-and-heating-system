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
heat_on = True
cool_on = True
tutorial_on = True

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

def setTempClicked():
    try:
        t = int(setTempValueInt.get())
        tempDiff = t - int(currentTemp)
        result = "You have set the temperature to %i Degrees Celsius!\n There is a %i Degree difference from the current temperature" %(t, tempDiff)
        selectedTemp.config(text=result)
    except ValueError as error:
        selectedTemp.config(title='Error', message=error)

def getTempClicked():
    curTemp = currentTemp
    result2 = "Current Temperature is : %s Degrees Celsius" %(curTemp)
    getTempValue.config(text=result2)

def toggleHeatClick():
    global heat_on
    if heat_on:
        result3 = "Heating : ON"
        heatingToggle.config(text=result3)
        heat_on = False
    else:
        result3 = "Heating : OFF"
        heatingToggle.config(text=result3)
        heat_on = True

def toggleCoolClick():
    global cool_on
    if cool_on:
        result4 = "Cooling : ON"
        coolingToggle.config(text=result4)
        cool_on = False
    else:
        result4 = "Cooling : OFF"
        coolingToggle.config(text=result4)
        cool_on = True

def tutorialClicked():
    global tutorial_on
    if tutorial_on:
        result5 = "By clicking 'Get Temperature' the current temperature reading is displayed.\nBy enterning a value into the box next to 'Set Temperature' and then clicking the button this allows you to select a specific temperature you would like the room to reach\nBy clicking 'Toggle Heating' the Biomass Heating is turned on\nBy clicking 'Toggle Cooling' the Cooling Fans are turned on\n You can also close the Tutorial text by clicking 'How to use' once again"
        tutorialText.config(text=result5)
        tutorial_on = False
    else:
        result5 = ""
        tutorialText.config(text=result5)
        tutorial_on = True

getTemp = tk.Button(frameButtons,text="Get Temperature")
getTemp.grid(row=0, column=0, sticky="ew", padx=5)
getTemp.configure(command=getTempClicked)

setTemp = tk.Button(frameButtons,text="Set Temperature")
setTemp.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
setTemp.configure(command=setTempClicked)

toggleHeating = tk.Button(frameButtons,text="Toggle Heating")
toggleHeating.grid(row=2, column=0, sticky="ew", padx=5)
toggleHeating.configure(command=toggleHeatClick)

toggleCooling = tk.Button(frameButtons,text="Toggle Cooling")
toggleCooling.grid(row=3, column=0, sticky="ew", padx=5)
toggleCooling.configure(command=toggleCoolClick)

tutorial = tk.Button(frameButtons,text="How to use")
tutorial.grid(row=4, column=0, sticky="ew", padx=5)
tutorial.configure(command=tutorialClicked)

setTempValueInt = IntVar()
setTempValue = Entry(answerWindow, bg="light yellow", textvariable=setTempValueInt)
setTempValue.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

getTempValue = tk.Label(answerWindow, text="Current Temperature is :")
getTempValue.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

selectedTemp = tk.Label(answerWindow)
selectedTemp.grid(row=5, column=0, sticky="ew", padx=5,pady=5)

heatingValue = StringVar()
heatingToggle = tk.Label(answerWindow, text="Heating default state is OFF")
heatingToggle.grid(row=2, column=0, sticky="ew", padx=5)

coolingToggle = tk.Label(answerWindow, text="Cooling default state is OFF")
coolingToggle.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

tutorialText = tk.Label(answerWindow, text="")
tutorialText.grid(row=4, column=0, sticky="ew", padx=5)

frameButtons.grid(row=0, column=0, sticky="ns")
answerWindow.grid(row=0, column=1, sticky="nsew")


root.mainloop()
