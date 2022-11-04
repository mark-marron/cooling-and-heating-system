# METHODS
# get temp? avg?
# set target temp for all zones
# manual override of fans
# manual override of heaters

# ATTRIBUTES
# target temp
# average temp

class adminControl():

    def __init__(self):
        self._target_temp = 22
        self._avg_temp = 22

    def get_temp(self):
        return self._avg_temp

    def set_temp(self, input_target):
        self._target_temp = input_target