import tkinter as tk
from tkinter import *
from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from TempSensor import TempSensor
import time as Time
import threading

running = True
adminPanel = AdminControl()
z1 = ZoneControl()
zonePanels = []
temp = z1.get_temp()
currentTempint = z1.get_zone_temp()
z1._state = 5
tutorial_on = True
statistics_on = True
setTempClicked = False

root = tk.Tk()

root.title('Heating and Cooling System Controller')
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure(1, minsize=200, weight=1)

answerWindow = tk.Frame(root)
frameButtons = tk.Frame(root, relief=tk.RAISED, bd=2)

label = tk.Label(text="Heating and Cooling System Controller", fg="black")

delay = 2

'''
power_used2 = threading.Timer(delay,z1.get_power_consumed())
power_used2.start()

money_spent = threading.Timer(delay,z1.get_cost_per_Kwh())
money_spent.start()
'''


def set_temp_clicked():
    try:
        t = int(setTempValueInt.get())
        z1._target_temp = int(setTempValueInt.get())
        set_time = tk.Button(frameButtons, text="Set time")
        set_time.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        set_time.configure(command=set_time_clicked)
        set_time_value = Entry(answerWindow, bg="light yellow", textvariable=setTimeValueInt)
        set_time_value.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

        if t < 0 or t > 30:
            result = "The temperature you have submitted (%i°C) is outside the recommended range! Please select a " \
                     "temperature between 0-30 degrees celsius" % t
            selectedTemp.config(text=result)

        elif (currentTempint != t) and (t >= 0 or t <= 30):
            # z1.new_temperature_physics()
            global setTempClicked
            setTempClicked = True
            start_time = threading.Timer(delay, z1.new_temperature_physics())
            start_time.start()
            power_used = threading.Timer(delay, z1.power_usage())
            power_used.start()
            if z1.get_zone_temp() > z1.get_zone_temp():
                z1._state = 1
                z1.new_temperature_physics()
            elif z1.get_zone_temp() < z1.get_zone_temp():
                z1._state = 4
                z1.new_temperature_physics()
            elif z1.get_zone_temp() == z1.get_zone_temp():
                z1._state = 5
            temp_diff = z1.get_target_temp() - currentTempint
            result = "You have set the temperature to %i °C!\n There is a %i Degree difference from the " \
                     "current temperature" % (z1.get_target_temp(), temp_diff)

            selectedTemp.config(text=result)
            if z1.get_state() == 4:
                result3 = "Heating : ON"
                result4 = "Cooling : OFF"
                heatingToggle.config(text=result3)
                coolingToggle.config(text=result4)
                z1._state = 4
            elif z1.get_state() == 1:
                result4 = "Cooling : ON"
                result3 = "Heating : OFF"
                coolingToggle.config(text=result4)
                heatingToggle.config(text=result3)
                z1._state = 1
            elif z1.get_state() == 5:
                result3 = "Heating : OFF"
                heatingToggle.config(text=result3)
                result4 = "Cooling : OFF"
                coolingToggle.config(text=result4)
                z1._state = 5
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
            result3 = "Heating : OFF"
            result4 = "Cooling : OFF"
            heatingToggle.config(text=result3)
            coolingToggle.config(text=result4)
            z1._state = 5
        selectedTime.config(text=result)
        answerWindow.update()
        Time.sleep(1)
        time = time - 1


'''
displays the current temperature outside to the user
'''


def get_temp_clicked():
    if setTempClicked:
        result2 = "Current Temperature is : %i °C" % z1.get_zone_temp()
        z1.new_temperature_physics()
    else:
        result2 = "Current Temperature is : %i °C" % int(TempSensor.get_outside_temp(TempSensor))
    getTempValue.config(text=result2)


'''
toggles the heating on and makes sure the cooling toggle cannot be on the same time as the heating
'''


def toggle_heat_click():
    if z1.get_state() == 4:
        z1._state = 5
    elif z1.get_state() != 4:
        z1._state = 4
    if z1.get_state() == 4:
        result3 = "Heating : ON"
        result4 = "Cooling : OFF"
        heatingToggle.config(text=result3)
        coolingToggle.config(text=result4)
        z1._state = 4
    else:
        result3 = "Heating : OFF"
        heatingToggle.config(text=result3)
        z1._state = 5


'''
toggles the cooling on and makes sure the cooling cant be on the same time as the heating
'''
'''
while z1._zone_temp > z1._target_temp:
    z1.new_temperature_physics
'''


def toggle_cool_click():
    if z1.get_state() == 1:
        z1._state = 5
    elif z1.get_state() != 1:
        z1._state = 1
    if z1.get_state() == 1:
        result4 = "Cooling : ON"
        result3 = "Heating : OFF"
        coolingToggle.config(text=result4)
        heatingToggle.config(text=result3)
        z1._state = 1
    else:
        result4 = "Cooling : OFF"
        coolingToggle.config(text=result4)
        z1._state = 5


'''
displays a text box to the user on how to use the interface to change the temperature settings
'''


def tutorial_clicked():
    global tutorial_on
    if tutorial_on:
        result5 = "By clicking 'Get Temperature' the current temperature reading is displayed.\n\nBy entering a value "\
                  "into the box next to 'Set Temperature' and then clicking the button this allows you to select a " \
                  "specific temperature you would like the room to reach\n\nBy clicking 'Toggle Heating' the Biomass " \
                  "Heating is turned on\n\nBy clicking 'Toggle Cooling' the Cooling Fans are turned on\n\n You can " \
                  "also " \
                  "close the Tutorial text by clicking 'How to use' once again "
        tutorialText.config(text=result5)
        tutorial_on = False
    else:
        result5 = ""
        tutorialText.config(text=result5)
        tutorial_on = True


'''
Displays statistics regarding amount of power used, money spent and how much money saved based on the current 
state of the system This is done by taking the heating and cooling into account and for how long they were on/off 
'''


def statistics_clicked():
    global statistics_on
    if statistics_on:
        power_usage.grid(row=2, column=1, sticky="ew", padx=5)
        money_spent.grid(row=3, column=1, sticky="ew", padx=5)
        money_saved.grid(row=4, column=1, sticky="ew", padx=5)
        result7 = ("Power usage (Kwh): %.2f" % get_power_usage())
        result8 = ("Money Spent (Euro): %.2f" % get_money_spent())
        result9 = ("Money Saved (Euro): %.2f" % get_money_saved())
        power_usage.config(text=result7)
        money_spent.config(text=result8)
        money_saved.config(text=result9)
        statistics_on = False
    elif not statistics_on:
        power_usage.grid_remove()
        money_spent.grid_remove()
        money_saved.grid_remove()
        statistics_on = True


'''
Returns the power usage amount for the statistics
'''


def get_power_usage():
    return z1.get_power_consumed()


'''
Returns the money spent amount for the statistics
This is done by getting the power usage amount and multiplying it by the cost per hour variable
'''


def get_money_spent():
    return get_power_usage() * z1.get_cost_per_kwh()


'''
Returns the money saved amount for the statistics
'''


def get_money_saved():
    return (get_power_usage() * z1.get_cost_per_kwh_radiator()) - (get_power_usage() * z1.get_cost_per_kwh())


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

statistics = tk.Button(frameButtons, text="Get Statistics")
statistics.grid(row=6, column=0, sticky="ew", padx=5)
statistics.configure(command=statistics_clicked)

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

power_usage = tk.Label(answerWindow, text="Power usage (Kwh): ")
money_spent = tk.Label(answerWindow, text="Money Spent (Euro): ")
money_saved = tk.Label(answerWindow, text="Money Saved (Euro): ")

frameButtons.grid(row=0, column=0, sticky="ns")
answerWindow.grid(row=0, column=1, sticky="nsew")

root.mainloop()
