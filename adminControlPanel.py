
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
        return self._time_remaining

    def set_timer(self, input_temp):
        self._time_remaining = input_temp

    def toggle_fan(self):
        pass

    def toggle_heater(self):
        pass
