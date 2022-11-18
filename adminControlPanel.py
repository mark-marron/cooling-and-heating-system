import time
import datetime

class AdminControl:

    def __init__(self):
        self._target_temp = 0
        self._avg_temp = 22
        self._time_remaining = 180  # Time in Seconds
        self._state = 5

    def get_avg_temp(self):
        return self._avg_temp

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
            if input_target > 0 and input_target < 30:
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
            self._timer = datetime.timedelta(seconds = self._total_seconds)
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