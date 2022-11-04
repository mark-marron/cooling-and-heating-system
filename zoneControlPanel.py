from tempSensor import tempSensor

class zoneControl():
    def __init__(self):
        self._temp_sensor = tempSensor()
        self._temp = self._temp_sensor.getTemp()
        self._heater_running = False
        self._fans_running = False

    def get_temp(self):
        return self._temp_sensor.getTemp()