from random import randint


class TempSensor:

    def __init__(self):
        self._temp = randint(18, 25)

    def get_temp(self):
        return self._temp
