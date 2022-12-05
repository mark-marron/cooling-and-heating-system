import time
import datetime
from TempSensor import TempSensor


class AdminControl:
    """
    Initializes variables - rooms, timer, timer_end_msg,total_seconds,target_temp,time_remaining, state, temp_sensor,
    temp
    """
    def __init__(self):
        self._rooms = ['kitchen', 'living room', 'bedroom1', 'bedroom2', 'dining room', 'hallway']
        self._timer = None  # Timer
        self._timer_end_msg = None  # Lets the user know the time is complete
        self._total_seconds = None  # total seconds
        self._target_temp = 0  # Target temperature
        self._time_remaining = 180  # Time in Seconds
        self._state = 5  # used to toggle heating and cooling
        self._temp_sensor = TempSensor()  # calling function TempSensor()
        self._temp = self._temp_sensor.get_outside_temp()
        self._prev_temps = []  # previous temperatures set

    '''
    Sets the Average temperature
    '''
    def avg_temp(self):
        avg_temp_list = []
        if avg_temp_list is not None:
            if len(avg_temp_list) >= 10:
                avg_temp_list.pop(0)
                avg_temp_list.append(int(self._temp))  # Cast to int for averaging operation, _temp inputs are str
            else:
                avg_temp_list.append(int(self._temp))
        return sum(avg_temp_list) / len(avg_temp_list)

    '''
    Returns the average temperature
    '''
    def get_avg_temp(self):
        return self.avg_temp()

    '''
    Returns the Average outside temperature - will be called every hour
    '''
    def get_avg_outside_temp(self):
        if len(self._prev_temps) < 24:
            self._prev_temps.append(int(self._temp_sensor.get_outside_temp()))
        else:
            self._prev_temps.pop(0)
            self._prev_temps.append(int(self._temp_sensor.get_outside_temp()))
        return sum(self._prev_temps) / len(self._prev_temps)

    '''
    Sets the target temperature - input from user cannot be another other than an integer in the range 0 - 30
    '''
    def set_target_temp(self, input_target):
        if type(input_target) == str:
            raise TypeError("Please enter a whole positive integer, not a string.")
        if type(input_target) == bool:
            raise TypeError("Please enter a whole positive integer, not a boolean.")
        if type(input_target) == list:
            raise TypeError("A positive integer number is supposed to be entered, not a list")
        if type(input_target) == dict:
            raise TypeError("A positive integer number is supposed to be entered, not a dictionary")
        if type(input_target) == int:
            if 0 < input_target < 30:
                self._target_temp = input_target
                if self._target_temp > int(TempSensor().get_outside_temp()):
                    if self._target_temp - int(TempSensor().get_outside_temp()) > 3:  # if there is more than a 3
                        # degree difference the biomass heating is turned on rather than the heatpump for heating
                        self._state = 4
                    else:
                        self._state = 3
                if self._target_temp < int(TempSensor().get_outside_temp()):
                    if int(TempSensor().get_outside_temp()) - self._target_temp > 3:  # if there is more than a 3
                        # degree difference the cooling fans are turned on rather than the heatpump for cooling
                        self._state = 1
                    else:
                        self._state = 2
                if self._target_temp == int(TempSensor().get_outside_temp()):   # if there is no temperature
                    # difference the state should be off as no heating or cooling needs to be done
                    self._state = 5
                return self._target_temp
            if input_target >= 30:
                self._target_temp = 30
                return self._target_temp
            if input_target <= 0:
                self._target_temp = 0
                return self._target_temp
        if type(input_target) == float:
            raise TypeError("Please enter a whole positive integer, not a float.")
        else:
            raise TypeError("You have entered the wrong type in please enter a positive integer between 0-30")

    '''
    Returns the target temperature
    '''
    def get_target_temp(self):
        return self._target_temp

    '''
    Returns current timer value and end message when total seconds = 0
    '''
    def get_timer(self):
        self._timer_end_msg = "Timer finished!"
        while self._total_seconds > 0:
            self._timer = datetime.timedelta(seconds=self._total_seconds)
            print(self._timer, end="\r")
            time.sleep(1)
            self._total_seconds = self._total_seconds - 1
        return self._timer_end_msg

    '''
    Sets the total seconds variable - how long the user wants the timer to be - must be an integer
    '''
    def set_timer(self, input_time):
        if type(input_time) == str:
            raise TypeError("A positive integer number is supposed to be entered, not a string")
        if type(input_time) == float:
            raise TypeError("A positive integer number is supposed to be entered, not a float")
        if type(input_time) == bool:
            raise TypeError("A positive integer number is supposed to be entered, not a boolean")
        if type(input_time) == list:
            raise TypeError("A positive integer number is supposed to be entered, not a list")
        if type(input_time) == dict:
            raise TypeError("A positive integer number is supposed to be entered, not a dictionary")
        if type(input_time) == int:
            if input_time < 0:
                raise ValueError("A positive integer number is supposed to be entered, not a negative value")
            if input_time > 0:
                self._total_seconds = int(input_time)
                return "time set"
        else:
            raise TypeError("You have entered the wrong type please enter a positive integer")

    '''
    Toggles fan
    sets state to 1
    '''
    def toggle_fan(self):
        self._state = 1

    '''
    Toggles heating
    sets state to 4
    '''
    def toggle_heater(self):
        self._state = 4
    
    '''
    Sets the rooms at which the admin can select to make temperature changes to
    '''
    def set_room(self):
        self._rooms = ['kitchen', 'living room', 'bedroom1', 'bedroom2', 'dining room', 'hallway']

    '''
    Returns the list of rooms for the admin
    '''
    def get_room(self):
        return self._rooms
    