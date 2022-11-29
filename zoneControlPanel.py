from TempSensor import TempSensor
from adminControlPanel import AdminControl
from random import randint
import asyncio
import time


class ZoneControl:
    """
    intializes variables - temp_sensor, target_temp, total_seconds, state, temp, heater_running and fans running
    """

    def __init__(self):
        self._temp_sensor = TempSensor()
        self._admin_control = AdminControl()
        self._target_temp = 0
        self._total_seconds = 0
        self._state = 5
        self._temp = int(self._temp_sensor.get_outside_temp())
        self._zone_temp = randint(8, 15)
        self._heater_running = False
        self._fans_running = False
        self._tminus_ambient_temp_decrease = 30  # Time is takes until _zone_temp decreases when Fan and Heating are
        # off, ambient temperature drop via losses
        self._tminus_ambient_temp_increase = 20
        self._tminus_temp_decrease = 5  # Time takes until _zone_temp decreases by 1 Degree
        self._tminus_temp_increase = 5   # Time takes until _zone_temp increases by 1 Degree
        self._start_time = 0
        self._time_taken = 0
        self._cost_per_Kwh = 0.24  # Cost in eur per Kilowatt hour (0.24 = euro 24c)
        self._power_consumed = 0  # Power in Kwh used by each heating/cooling option set in function power_usage

    ''' 
    state:
    1 = fan
    2 = heatpump cooling
    3 = heatpump heating
    4 = biomass heating
    5 = off
    '''

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
        self._target_temp = self._admin_control.set_target_temp(input_target)
        self._start_time = int(time.time())

    '''
    Gets the target temperature through the admin control panel
    and returns this value
    '''

    def get_target_temp(self):
        self._target_temp = self._admin_control.get_target_temp()
        return self._target_temp

    '''
    Sets the timer value total seconds with user input through admin control panel
    '''

    def set_timer(self, input_time):
        self._total_seconds = self._admin_control.set_timer(input_time)

    '''
    returns the timer value from the admin control panel
    '''

    def get_timer(self):
        return self._admin_control.get_timer()

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

    async def temperature_physics(self):
        if self._target_temp > self._zone_temp:
            self.toggle_heater()
        elif self._target_temp < self._zone_temp:
            self.toggle_fan()

        if self.get_state() == 5:  # If heating and fan are off
            if self._zone_temp > self._temp:
                self._zone_temp -= 1
                await asyncio.sleep(self._tminus_ambient_temp_decrease)  # 1 deg decrease in temp via ambient losses
            elif self._zone_temp < self._temp:
                self._zone_temp += 1
                await asyncio.sleep(self._tminus_ambient_temp_increase)
            elif self._zone_temp == self._temp:
                self._zone_temp = self._temp

        elif self.get_state() == 4:  # If heating is on
            if self._target_temp == self._zone_temp:
                self.reset_state()  # Turn heating off
            elif self._target_temp > self._zone_temp:
                self._zone_temp += 1
                await asyncio.sleep(self._tminus_temp_increase)  # 1C increase in temp takes _tminus_temp_increase sec
            elif self._target_temp < self._zone_temp:
                self.toggle_fan()
                await asyncio.sleep(self._tminus_temp_decrease)  # 1C decrease in temp takes _tminus_temp_decrease sec

        elif self.get_state() == 1:  # If fan is on
            if self._target_temp == self._zone_temp:
                self.reset_state()
            elif self._target_temp < self._zone_temp:
                self._zone_temp -= 1
                await asyncio.sleep(self._tminus_temp_decrease)  # 1C decrease in temp takes _tminus_temp_increase sec
            elif self._target_temp > self._zone_temp:
                self.toggle_heater()
                await asyncio.sleep(self._tminus_temp_decrease)  # 1C increase in temp takes _tminus_temp_decrease sec

    def new_temperature_physics(self):
        self._time_taken = int(time.time() - self._start_time)
        t2 = self._time_taken

        if self._target_temp > self._zone_temp:
            self.toggle_heater()
        elif self._target_temp < self._zone_temp:
            self.toggle_fan()

        if self.get_state() == 5:  # If heating and fan are off
            if self._zone_temp > self._temp:
                if (t2 % self._tminus_ambient_temp_decrease == 0) and (t2 != 0):
                    self._zone_temp -= (3/self._tminus_ambient_temp_decrease)  # Checking if
                    # _tminus_ambient_temp_decrease has elapsed, if so minus the multiple of that time that has elapsed
                    self._start_time = time.time()  # reset start time
            elif self._zone_temp < self._temp:
                if (t2 % self._tminus_ambient_temp_increase == 0) and (t2 != 0):
                    self._zone_temp += (3 / self._tminus_ambient_temp_increase)  # Checking if
                    # _tminus_ambient_temp_increase has elapsed, if so add the multiple of that time that has elapsed
                    self._start_time = time.time()  # reset start time
            elif self._zone_temp == self._temp:
                self._zone_temp = self._temp

        elif self.get_state() == 4:  # If heating is on
            if self._target_temp == self._zone_temp:
                self.reset_state()  # Turn heating off
            elif self._target_temp > self._zone_temp:
                if (t2 % self._tminus_temp_increase == 0) and (t2 != 0):
                    self._zone_temp += (3/self._tminus_temp_increase)  # Checking if _tminus_temp_increase seconds
                    # has elapsed, if so add the multiple of that time that has
                    self._start_time = time.time()  # reset start time
            elif self._target_temp < self._zone_temp:
                self.toggle_fan()

        elif self.get_state() == 1:  # If fan is on
            if self._target_temp == self._zone_temp:
                self.reset_state()
            elif self._target_temp < self._zone_temp:
                if (t2 % self._tminus_temp_decrease == 0) and (t2 != 0):
                    self._zone_temp -= (3 / self._tminus_temp_decrease)  # Checking if _tminus_temp_decrease seconds
                    # has elapsed, if so minus the multiple of that time that has elapsed
                    self._start_time = time.time()  # reset start time
            elif self._target_temp > self._zone_temp:
                self.toggle_heater()

    def power_usage(self):
        if self.get_state() == 5:
            self._power_consumed = 0

        elif self.get_state() == 4:
            self._power_consumed = 6

        elif self.get_state() == 3:
            self._power_consumed = 2

        elif self.get_state() == 2:
            self._power_consumed = 3

        elif self.get_state() == 1:
            self._power_consumed = 0.05


