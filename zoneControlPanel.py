from TempSensor import TempSensor


class ZoneControl:
    def __init__(self):
        self._temp_sensor = TempSensor()
        self._temp = self._temp_sensor.get_temp()
        self._heater_running = False
        self._fans_running = False

    def get_temp(self):
        return self._temp_sensor.get_temp()
