from random import randint

class tempSensor():
    def __init__(self):
        self._temp = randint(18, 25)

    def getTemp(self):
        return self._temp