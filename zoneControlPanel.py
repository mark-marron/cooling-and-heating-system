from TempSensor import TempSensor
from adminControlPanel import AdminControl
from time import sleep
from random import randint


class ZoneControl:
    """
    intializes variables - temp_sensor, target_temp, total_seconds, state, temp, heater_running and fans running
    """

    def __init__(self):
        self._temp_sensor = TempSensor()
        self._target_temp = 0
        self._total_seconds = 0
        self._state = 5
        self._temp = self._temp_sensor.get_outside_temp()
        self._zone_temp = randint(8, 15)
        self._heater_running = False
        self._fans_running = False
        self._tminus_ambient_temp_decrease = 30  # Time is takes until _zone_temp decreases when Fan and Heating are
        # off, ambient temperature drop via losses
        self._tminus_temp_decrease = 5  # Time takes until _zone_temp decreases by 1 Degree
        self._tminus_temp_increase = 5   # Time takes until _zone_temp increases by 1 Degree

    '''
    Returns the temperature value for the temp sensor class
    '''

    def get_temp(self):
        return self._temp_sensor.get_outside_temp()

    def get_zone_temp(self):
        return self._zone_temp

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
        self._total_seconds = AdminControl.set_timer(AdminControl, input_time)

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

    def get_state(self):
        return self._state

    def reset_state(self):
        self._state = 5

    def temperature_physics(self):
        if self._target_temp > self._zone_temp:
            self.toggle_heater()
        elif self._target_temp < self._zone_temp:
            self.toggle_fan()

        if self.get_state() == 5:  # If heating and fan are off
            if self._zone_temp > self._temp:
                self._temp -= 1
                sleep(self._tminus_ambient_temp_decrease)  # 1 deg decrease in temp via ambient losses
            elif self._zone_temp <= self._temp:
                self._zone_temp = self._temp

        elif self.get_state() == 4:  # If heating is on
            if self._target_temp == self._zone_temp:
                self.reset_state()  # Turn heating off
            elif self._target_temp > self._zone_temp:
                self._zone_temp += 1
                sleep(self._tminus_temp_increase)  # 1 deg increase in temp takes _tminus_temp_increase seconds
            elif self._target_temp < self._zone_temp:
                self.toggle_fan()
                sleep(self._tminus_temp_decrease)  # 1 deg decrease in temp takes _tminus_temp_decrease seconds

        elif self.get_state() == 1:  # If fan is on
            if self._target_temp == self._zone_temp:
                self.reset_state()
            elif self._target_temp < self._zone_temp:
                self._zone_temp -= 1
                sleep(self._tminus_temp_decrease)  # 1 deg decrease in temp takes _tminus_temp_increase seconds
            elif self._target_temp > self._zone_temp:
                self.toggle_heater()
                sleep(self._tminus_temp_decrease)  # 1 deg increase in temp takes _tminus_temp_decrease seconds
