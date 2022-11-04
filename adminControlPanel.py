
class adminControl():

    def __init__(self):
        self._target_temp = 22
        self._avg_temp = 22

    def get_avg_temp(self):
        return self._avg_temp

    def set_target_temp(self, input_target):
        self._target_temp = input_target

    def toggleFan(self):
        pass

    def toggleHeater(self):
        pass