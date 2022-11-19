import tkinter as tk
from tkinter import *
from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from TempSensor import TempSensor
import time as Time

running = True
adminPanel = AdminControl()
z1 = ZoneControl()
zonePanels = []
temp = TempSensor
currentTempint = z1.get_temp()
currentTemp = str(currentTempint)
heat_on = True
cool_on = True
tutorial_on = True

root = tk.Tk()

root.title('Heating and Cooling System Controller')
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure(1, minsize=200, weight=1)

answerWindow = tk.Frame(root)
frameButtons = tk.Frame(root, relief=tk.RAISED, bd=2)

label = tk.Label(text="Heating and Cooling System Controller", fg="black")

'''When set temp button is clicked the target temp value is set to the users inputted value a message is displayed to 
tell the user they have set the temperature and what the current difference in temp is from the outside temperature 
also gives the user the option to set a timer once set temp is clicked '''


def set_temp_clicked():
    try:
        t = int(setTempValueInt.get())
        set_time = tk.Button(frameButtons, text="Set time")
        set_time.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        set_time.configure(command=set_time_clicked)
        set_time_value = Entry(answerWindow, bg="light yellow", textvariable=setTimeValueInt)
        set_time_value.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

        if t < 0 or t > 30:
            result = "The temperature you have submitted (%i) is outside the recommended range! Please select a " \
                     "temperature between 0-30 degrees celsius" % t
            selectedTemp.config(text=result)

        else:
            temp_diff = t - int(currentTemp)
            result = "You have set the temperature to %i Degrees Celsius!\n There is a %i Degree difference from the " \
                     "current temperature" % (t, temp_diff)
            selectedTemp.config(text=result)
    except ValueError as error:
        selectedTemp.config(title='Error', message=error)


'''
allows the user to set a timer for the heating/ cooling to turn off once it reaches 0
'''


def set_time_clicked():
    time = int(setTimeValueInt.get())
    adminPanel.set_timer(time)
    while time > -1:
        if time > 0:
            result = "time : %i" % time
        else:
            result = "time is up!"
        selectedTime.config(text=result)
        answerWindow.update()
        Time.sleep(1)
        time = time - 1


'''
displays the current temperature outside to the user
'''


def get_temp_clicked():
    cur_temp = currentTemp
    result2 = "Current Temperature is : %s Degrees Celsius" % cur_temp
    getTempValue.config(text=result2)


'''
toggles the heating on and makes sure the cooling toggle cannot be on the same time as the heating
'''


def toggle_heat_click():
    global heat_on
    global cool_on
    if heat_on:
        result3 = "Heating : ON"
        result4 = "Cooling  : OFF"
        heatingToggle.config(text=result3)
        coolingToggle.config(text=result4)
        heat_on = False
        cool_on = True
    else:
        result3 = "Heating : OFF"
        heatingToggle.config(text=result3)
        heat_on = True


'''
toggles the cooling on and makes sure the cooling cant be on the same time as the heating
'''


def toggle_cool_click():
    global cool_on
    global heat_on
    if cool_on:
        result4 = "Cooling : ON"
        result3 = "Heating : OFF"
        coolingToggle.config(text=result4)
        heatingToggle.config(text=result3)
        cool_on = False
        heat_on = True
    else:
        result4 = "Cooling : OFF"
        coolingToggle.config(text=result4)
        cool_on = True


'''
displays a text box to the user on how to use the interface to change the temperature settings
'''


def tutorial_clicked():
    global tutorial_on
    if tutorial_on:
        result5 = "By clicking 'Get Temperature' the current temperature reading is displayed.\nBy enterning a value " \
                  "into the box next to 'Set Temperature' and then clicking the button this allows you to select a " \
                  "specific temperature you would like the room to reach\nBy clicking 'Toggle Heating' the Biomass " \
                  "Heating is turned on\nBy clicking 'Toggle Cooling' the Cooling Fans are turned on\n You can also " \
                  "close the Tutorial text by clicking 'How to use' once again "
        tutorialText.config(text=result5)
        tutorial_on = False
    else:
        result5 = ""
        tutorialText.config(text=result5)
        tutorial_on = True


getTemp = tk.Button(frameButtons, text="Get Temperature")
getTemp.grid(row=0, column=0, sticky="ew", padx=5)
getTemp.configure(command=get_temp_clicked)

setTemp = tk.Button(frameButtons, text="Set Temperature")
setTemp.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
setTemp.configure(command=set_temp_clicked)

toggleHeating = tk.Button(frameButtons, text="Toggle Heating")
toggleHeating.grid(row=2, column=0, sticky="ew", padx=5)
toggleHeating.configure(command=toggle_heat_click)

toggleCooling = tk.Button(frameButtons, text="Toggle Cooling")
toggleCooling.grid(row=3, column=0, sticky="ew", padx=5)
toggleCooling.configure(command=toggle_cool_click)

tutorial = tk.Button(frameButtons, text="How to use")
tutorial.grid(row=4, column=0, sticky="ew", padx=5)
tutorial.configure(command=tutorial_clicked)

setTimeValueInt = IntVar()

setTempValueInt = IntVar()
setTempValue = Entry(answerWindow, bg="light yellow", textvariable=setTempValueInt)
setTempValue.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

getTempValue = tk.Label(answerWindow, text="Current Temperature is :")
getTempValue.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

selectedTemp = tk.Label(answerWindow)
selectedTemp.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

heatingValue = StringVar()
heatingToggle = tk.Label(answerWindow, text="Heating default state is OFF")
heatingToggle.grid(row=2, column=0, sticky="ew", padx=5)

coolingToggle = tk.Label(answerWindow, text="Cooling default state is OFF")
coolingToggle.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

selectedTime = tk.Label(answerWindow)
selectedTime.grid(row=5, column=1, sticky="ew", padx=5, pady=15)

tutorialText = tk.Label(answerWindow, text="")
tutorialText.grid(row=4, column=0, sticky="ew", padx=5)

frameButtons.grid(row=0, column=0, sticky="ns")
answerWindow.grid(row=0, column=1, sticky="nsew")

root.mainloop()
