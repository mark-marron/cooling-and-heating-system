import time
import datetime

class AdminControl:

    def __init__(self):
        self._target_temp = 22
        self._avg_temp = 22
        self._time_remaining = 180  # Time in Seconds

    def get_avg_temp(self):
        return self._avg_temp

    def set_target_temp(self, input_target):
        self._target_temp = input_target

    def get_timer(self):
        self._timer_end_msg = "Timer finished!"
        while self._total_seconds > 0:
            self._timer = datetime.timedelta(seconds = self._total_seconds)
            print(self._timer, end="\r")
            time.sleep(1)
            self._total_seconds = self._total_seconds - 1
        return self._timer_end_msg
        

    def set_timer(self, input_time):
        self._total_seconds = input_time
        return "time set"
        

    def toggle_fan(self):
        pass

    def toggle_heater(self):
        pass
