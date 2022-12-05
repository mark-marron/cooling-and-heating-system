from TempSensor import TempSensor
from adminControlPanel import AdminControl
from random import randint
import time


class ZoneControl:
    """
    initializes variables - temp_sensor, target_temp, total_seconds, state, temp, heater_running and fans running
    """

    def __init__(self):
        self._temp_sensor = TempSensor()
        self._admin_control = AdminControl()
        self._target_temp = 0
        self._total_seconds = 0
        self._state = 5
        self._temp = int(self._temp_sensor.get_outside_temp())
        self._zone_temp = randint(8, 15)
        self._tminus_ambient_temp_decrease = 30  # Time is takes until _zone_temp decreases when Fan and Heating are
        # off, ambient temperature drop via losses
        self._tminus_ambient_temp_increase = 20
        self._tminus_temp_decrease = 5  # Time takes until _zone_temp decreases by 1 Degree
        self._tminus_temp_increase = 5   # Time takes until _zone_temp increases by 1 Degree
        self._start_time = 0
        self._time_taken = 0
        self._cost_per_Kwh = 0.24  # Cost in eur per Kilowatt hour (0.24 = euro 24c)
        self._cost_per_Kwh_Raditors = 0.26 # Cost in eur per Kilowatt hour if the heating source was a radiator as opposed to heat pump/ biomass heating (0.26 = euro 26c)
        self._power_consumed = 0  # Power in Kwh used by each heating/cooling option set in function power_usage

    '''
    Returns the temperature value for the temp sensor class 
    '''

    def get_temp(self):
        return self._temp_sensor.get_outside_temp()

    '''
    Returns the current zone temperature
    '''

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
    Returns the power consumed by the heating and cooling systems in the zone
    '''

    def get_power_consumed(self):
        return self._power_consumed

    '''
    Returns the current cost per Kwh
    '''

    def get_cost_per_Kwh(self):
        return self._cost_per_Kwh

    '''
    Returns the current cost per Kwh of a radiator
    '''

    def get_cost_per_Kwh_Radiator(self):
        return self._cost_per_Kwh_Raditors


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

    '''
    Returns the current state of the heating/cooling system
    1 = fan
    2 = heatpump cooling
    3 = heatpump heating
    4 = biomass heating
    5 = off
    '''

    def get_state(self):
        return self._state

    '''
    Turns off any heaters or coolers
    sets state to 5
    '''

    def reset_state(self):
        self._state = 5

    def new_temperature_physics(self):
        if self._start_time == 0:
            self._start_time = int(time.time())
        self._time_taken = int(time.time() - self._start_time)
        print("start time: ", self._start_time)
        print("time taken: ", self._time_taken)

        if self._target_temp > self._zone_temp:
            self.toggle_heater()
        elif self._target_temp < self._zone_temp:
            self.toggle_fan()

        if self.get_state() == 5:  # If heating and fan are off
            if self._zone_temp > self._temp:
                if (self._time_taken % self._tminus_ambient_temp_decrease == 0) and (self._time_taken != 0):
                    self._zone_temp -= int(self._time_taken / self._tminus_ambient_temp_decrease)  # Checking if
                    # _tminus_ambient_temp_decrease has elapsed, if so minus the multiple of that time that has elapsed
                    self._start_time = time.time()  # reset start time
            elif self._zone_temp < self._temp:
                if (self._time_taken % self._tminus_ambient_temp_increase == 0) and (self._time_taken != 0):
                    self._zone_temp += int(self._time_taken / self._tminus_ambient_temp_increase)  # Checking if
                    # _tminus_ambient_temp_increase has elapsed, if so add the multiple of that time that has elapsed
                    self._start_time = time.time()  # reset start time
            elif self._zone_temp == self._temp:
                self._zone_temp = self._temp

        elif self.get_state() == 4:  # If heating is on
            if self._target_temp == self._zone_temp:
                self.reset_state()  # Turn heating off
            elif self._target_temp > self._zone_temp:
                if (self._time_taken % self._tminus_temp_increase == 0) and (self._time_taken != 0):
                    self._zone_temp += int(self._time_taken / self._tminus_temp_increase)  # Checking if
                    # _tminus_temp_increase seconds has elapsed, if so add the multiple of that time that has
                    self._start_time = time.time()  # reset start time
                    self.power_usage()
            elif self._target_temp < self._zone_temp:
                self.toggle_fan()

        elif self.get_state() == 1:  # If fan is on
            if self._target_temp == self._zone_temp:
                self.reset_state()
            elif self._target_temp < self._zone_temp:
                if (self._time_taken % self._tminus_temp_decrease == 0) and (self._time_taken != 0):
                    self._zone_temp -= int(self._time_taken / self._tminus_temp_decrease)  # Checking if
                    # _tminus_temp_decrease seconds has elapsed, if so minus the multiple of that time that has elapsed
                    self._start_time = time.time()  # reset start time
                    self.power_usage()
            elif self._target_temp > self._zone_temp:
                self.toggle_heater()

    def power_usage(self):
        if self.get_state() == 5:
            self._power_consumed += 0

        elif self.get_state() == 4:
            self._power_consumed += 6

        elif self.get_state() == 3:
            self._power_consumed += 2

        elif self.get_state() == 2:
            self._power_consumed += 3

        elif self.get_state() == 1:
            self._power_consumed += 0.05
