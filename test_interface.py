from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
import unittest

adminPanel = AdminControl()
z1 = ZoneControl()
zonePanels = []
temp = z1._temp
currentTempint = z1.get_zone_temp()
z1._state = 5

delay = 2

def set_temp_clicked(temp):
        t = temp
        if t >= 0 and t <= 30:
            t= t
            return t
    
        if t > 30:
            t = 30
            return t
        if t < 0:
            t = 0
            return t
        else:
            return currentTempint

'''
toggles the heating on and makes sure the cooling toggle cannot be on the same time as the heating
'''

def toggle_heat_click(toggle):
    if toggle == 4:
        z1._state = 5
    elif toggle != 4:
        z1._state = 4
    if toggle==4:
        z1._state = 4 
    else:
        z1._state = 5
    return z1._state
'''
toggles the cooling on and makes sure the cooling cant be on the same time as the heating
'''
'''
while z1._zone_temp > z1._target_temp:
    z1.new_temperature_physics
'''
def toggle_cool_click(toggle):
    if toggle == 1:
        z1._state = 5
    elif toggle != 1:
        z1._state = 1
    if toggle==1:
        z1._state = 1
    else:
        z1._state = 5
    return z1._state

'''
allows the user to set a timer for the heating/ cooling to turn off once it reaches 0
'''


def set_time_clicked(t):
    time = t
    adminPanel.set_timer(time)
    result = time
    """while time > -1:
        if time > 0:
            result = time
        else:
            result = time
        time = time - 1 """
    return result


#PARTITION 1 if the target temperature entered by the user is above 30 or below 0 it is not valid
class TestsetTempInterfaceInvalid(unittest.TestCase):
     def test_set_temp_clicked(self):
        self.assertAlmostEqual(set_temp_clicked(500), 30)
        self.assertAlmostEqual(set_temp_clicked(-20), 0)

#PARTITION 2 if the target temperature entered by the user is between 0 and 30 the input is valid
class TestsetTempInterfaceValid(unittest.TestCase):
    def test_set_temp_clicked(self):
        self.assertAlmostEqual(set_temp_clicked(30),30)
        self.assertAlmostEqual(set_temp_clicked(0),0)

#PARTITION 3 if the user toggles the heating on the state is X and cooling is off
class TestToggleHeatInterface(unittest.TestCase):
    def test_toggle_heat_clicked(self):
        self.assertAlmostEqual(toggle_heat_click(4),4)
        self.assertAlmostEqual(toggle_heat_click(3),5)

#PARTITION 4 if the user toggles the cooling on the state is y and heating is off
class TestToggleCoolInterface(unittest.TestCase):
    def test_toggle_cool_clicked(self):
        self.assertAlmostEqual(toggle_cool_click(1),1)
        self.assertAlmostEqual(toggle_cool_click(2),5)

#PARTITION 5 if both heating and cooling are off the state is z (5)
class TestToggleCoolandHeatInterface(unittest.TestCase):
    def test_toggle_cool_heat_not_clicked(self):
        self.assertAlmostEqual(z1._state, 5)
        toggle_cool_click(1)
        self.assertAlmostEqual(z1._state, 1)

#PARTITION 6 if the user inputs a value below 0 when setting the time the input is not valid
class TestsetTimeInterfaceInvalid(unittest.TestCase):
    def test_set_time_clicked(self):
        self.assertRaises(ValueError, set_time_clicked, -12)

#PARTITION 7 if the user inputs a value that is equal to or greater than 0 the number is valid
class TestsetTimeInterfaceValid(unittest.TestCase):
    def test_set_time_clicked(self):
        self.assertAlmostEqual(set_time_clicked(15), 15)



