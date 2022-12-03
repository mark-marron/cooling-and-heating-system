import unittest
from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from TempSensor import TempSensor

"""
This test suite was developed for blackbox testing
The standard user interface was dismantles and a seperate 'client' was created that invokes the same methods that are used in the adminInterface.py file
The methods needed to be altered to take in parameters as in the there original state the values were input into the methods through the use of .gets() and so on
Furthermore for the methods to be suitable for testing, instead of displaying the result of the method execution to the gui it now returns the value
This is needed for unit testing for using statements such as assertAlmostEqual as it needs a returned value for the method to test against the expected value
The reaons values are returned rather than exceptions raised in these methods is due to the fact that when the user interacts with the interface, they do not see exceptions (they only show up in the terminal)
Hence in tests where a value is invalid a default value may be returned or in the case of get_settings() a string saying 'Nothign was set' was returned
When creating these tests the partitions were outlined first to help get a sense of what tests needed to be executed
Then the inputs were organized into various ranges of inputs into eq classes and one value was picked per class
In the case where a test case failed the method was then updated in order for the test to pass
This led to a good bit of test driven style development.
"""

#PARTITION 1 if the target temperature entered by the user is above 30 or below 0 it is not valid
class TestsetTempAdminInterfaceInvalid(unittest.TestCase):
     def test_set_temp_clicked(self):
        self.assertAlmostEqual(set_temp_clicked(500), 30)
        self.assertAlmostEqual(set_temp_clicked(-20), 0)

#PARTITION 2 if the target temperature entered by the user is between 0 and 30 the input is valid
class TestsetTempAdminInterfaceValid(unittest.TestCase):
    def test_set_temp_clicked(self):
        self.assertAlmostEqual(set_temp_clicked(30),30)
        self.assertAlmostEqual(set_temp_clicked(0),0)

#PARTITION 3 if the user toggles the heating on the state is X and cooling is off
class TestToggleHeatAdminInterface(unittest.TestCase):
    def test_toggle_heat_clicked(self):
        self.assertAlmostEqual(toggle_heat_click(1),4)
        self.assertAlmostEqual(toggle_heat_click(3),5)

#PARTITION 4 if both heating and cooling are off the state is z (5)
class TestToggleCoolandHeatAdminInterface(unittest.TestCase):
    def test_toggle_cool_heat_not_clicked(self):
        self.assertAlmostEqual(z1._state, 5)
        toggle_cool_click(1)
        self.assertAlmostEqual(z1._state, 1)

#PARTITION 5 if the user toggles the cooling on the state is y and heating is off
class TestToggleCoolAdminInterface(unittest.TestCase):
    def test_toggle_cool_clicked(self):
        self.assertAlmostEqual(toggle_cool_click(1),1)
        self.assertAlmostEqual(toggle_cool_click(2),5)

#PARTITION 6 if the user inputs a value below 0 when setting the time the input is not valid
class TestsetTimeAdminInterfaceInvalid(unittest.TestCase):
    def test_set_time_clicked(self):
        self.assertRaises(ValueError, set_time_clicked, -12)

#PARTITION 7 if the user inputs a value that is equal to or greater than 0 the number is valid
class TestsetTimeAdminInterfaceValid(unittest.TestCase):
    def test_set_time_clicked(self):
        self.assertAlmostEqual(set_time_clicked(15), 15)

#PARTITION 8 if the user selects a room that is not on the list of rooms the input is invalid
class TestSetRoomAdminInterfaceInvalid(unittest.TestCase):
    def test_set_room_clicked(self):
        self.assertAlmostEqual(set_room('not_valid_room'),'kitchen')

#PARTITION 9 if the user selects a room that is on the list of rooms the input is valid
class TestSetRoomAdminInterfaceValid(unittest.TestCase):
    def test_set_room_clicked(self):
        self.assertAlmostEqual(set_room('bedroom2'),'bedroom2')

#PARTITION 10 if the user saves the settings without setting any the input is invalid
class TestSetSettingsAdminInterfaceInvalid(unittest.TestCase):
    def test_set_settings_clicked(self):
        self.assertAlmostEqual(set_settings(None,None),('kitchen',currentTempInt))

#PARTITION 11 if the user saves the settings and there are inputs set the input is valid
class TestSetSettingsAdminInterfaceValid(unittest.TestCase):
    def test_set_settings_clicked(self):
        self.assertAlmostEqual(set_settings('hallway',21),('hallway',21))

#PARTITION 12 if the user loads settings without setting saving any settings the it is invalid
class TestGetSettingsAdminInterfaceInvalid(unittest.TestCase):
    def test_get_settings_clicked(self):
        self.assertAlmostEqual(get_settings(),'Nothing was set')

#PARTITION 13 if th euser loads settings after saving a number of settings the it is valid 
class TestGetSettingsAdminInterfaceValid(unittest.TestCase):
    def test_get_settings_clicked(self):
        set_settings('bedroom1',17)
        self.assertAlmostEqual(get_settings(),'Settings')




running = True
adminPanel = AdminControl()
z1 = ZoneControl()
zonePanels = []
temp = TempSensor
currentTempInt = z1.get_temp()
currentTemp = str(currentTempInt)
heat_on = True
cool_on = True
called = False
options = adminPanel.get_room()
settingsDict = {}

'''When set temp button is clicked the target temp value is set to the users inputted value a message is displayed to 
tell the user they have set the temperature and what the current difference in temp is from the outside temperature 
also gives the user the option to set a timer once set temp is clicked '''
def set_temp_clicked(temp):
    t = temp
    if t < 0:
        t = 0
    if t > 30:
        t=30
    else:
        t = t
    return t



'''
allows the user to set a timer for the heating/ cooling to turn off once it reaches 0
'''
def set_time_clicked(t):
    time = t
    adminPanel.set_timer(time)
    """
    while time > -1:
        if time > 0:
            result = "time : %i" % time
        else:
            result = "time is up!"
        time = time - 1
    """
    return time

'''
toggles the heating on and makes sure the cooling toggle cannot be on the same time as the heating
'''
def toggle_heat_click(toggle):
    global heat_on
    global cool_on
    if toggle == 1:
        result3 = "Heating : ON"
        result4 = "Cooling  : OFF"
        heat_on = False
        cool_on = True
        z1._state = 4
    else:
        result3 = "Heating : OFF"
        heat_on = True
        z1._state = 5
    return z1._state


'''
toggles the cooling on and makes sure the cooling cant be on the same time as the heating
'''
def toggle_cool_click(toggle):
    global cool_on
    global heat_on
    if toggle == 1:
        result4 = "Cooling : ON"
        result3 = "Heating : OFF"
        cool_on = False
        heat_on = True
        z1._state = 1
    else:
        result4 = "Cooling : OFF"
        cool_on = True
        z1._state = 5
    return z1._state

def set_room(room):
    result = "Room selected : %s" %(room)
    for i in options:
        if room == i:
            return room
    else:
        return options[0]


def set_settings(roomParam,temp):
    global called
    called = True
    for i in options:
        if roomParam == i:
            room = roomParam
        else:
            room = options[0]
    t = temp
    if type(t) != int:
        t = currentTempInt
        return room,t
    if t < 0:
        t = 0
        return room,int(t)
    if t > 30:
        t=30
        return room,int(t)
    if t >= 0 and t <= 30:
        return room,int(t)
    else:
        t = currentTempInt
        return room,int(t)
    

def get_settings():
    if called == True:
        return 'Settings'
    else:
        return 'Nothing was set'
    
