import time
import datetime
from TempSensor import TempSensor


class AdminControl:

    def __init__(self):
        self._rooms = None
        self._timer = None
        self._timer_end_msg = None
        self._total_seconds = None
        self._target_temp = 0
        self._time_remaining = 180  # Time in Seconds
        self._state = 5
        self._temp_sensor = TempSensor()
        self._temp = self._temp_sensor.get_outside_temp()

    def avg_temp(self):
        avg_temp_list = []
        if avg_temp_list is not None:
            if len(avg_temp_list) >= 10:
                avg_temp_list.pop(0)
                avg_temp_list.append(int(self._temp))  # Cast to int for averaging operation, _temp inputs are str
            else:
                avg_temp_list.append(int(self._temp))
        return sum(avg_temp_list) / len(avg_temp_list)

    def get_avg_temp(self):
        return self.avg_temp()

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
            if input_target >= 30:
                self._target_temp = 30
            if input_target <= 0:
                self._target_temp = 0
        if type(input_target) == float:
            raise TypeError("Please enter a whole positive integer, not a float.")

    def get_target_temp(self):
        return self._target_temp

    def get_timer(self):
        self._timer_end_msg = "Timer finished!"
        while self._total_seconds > 0:
            self._timer = datetime.timedelta(seconds=self._total_seconds)
            print(self._timer, end="\r")
            time.sleep(1)
            self._total_seconds = self._total_seconds - 1
        return self._timer_end_msg

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
                self._total_seconds = input_time
                return "time set"

    def toggle_fan(self):
        self._state = 1

    def toggle_heater(self):
        self._state = 4
    
    def set_room(self):
        self._rooms = ['kitchen', 'living room', 'bedroom1', 'bedroom2', 'dining room', 'hallway']

    def get_room(self):
        return self._rooms
    