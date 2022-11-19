from TempSensor import TempSensor
from adminControlPanel import AdminControl

class ZoneControl:
    '''
    intializes variables - temp_sensor, target_temp, total_seconds, state, temp, heater_running and fans running
    '''
    def __init__(self):
        self._temp_sensor = TempSensor()
        self._target_temp = 0
        self._total_seconds = 0
        self._state = 5
        self._temp = self._temp_sensor.get_outside_temp()
        self._heater_running = False
        self._fans_running = False

    '''
    Returns the temperature value for the temp sensor class
    '''
    def get_temp(self):
        return self._temp_sensor.get_outside_temp()


    '''
    Sets the target temperature through the admin control panel
    '''
    def set_target_temp(self, input_target):
        AdminControl.set_target_temp(AdminControl, input_target)

    '''
    Gets the target temperature through the admin control panel
    and returns this value
    '''
    def get_target_temp(self):
        self._target_temp = AdminControl.get_target_temp(AdminControl)
        return self._target_temp

    '''
    Sets the timer value total seconds with user input through admin control panel
    '''
    def set_timer(self, input_time):
        self._total_seconds = AdminControl.set_timer(AdminControl,input_time)
        
    '''
    returns the timer value from the admin control panel
    ''' 
    def get_timer(self):
        return AdminControl.get_timer(AdminControl)

    '''
    Toggles the fans
    sets state to 1
    '''
    def toggle_fan(self):
        self._state = 1

    '''
    Toggles the heater
    sets state to 4
    '''
    def toggle_heater(self):
        self._state = 4