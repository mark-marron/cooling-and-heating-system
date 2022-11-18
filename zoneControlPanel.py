from TempSensor import TempSensor
from adminControlPanel import AdminControl

class ZoneControl:
    def __init__(self):
        self._temp_sensor = TempSensor()
        self._target_temp = 0
        self._total_seconds = 0
        self._state = 5
        self._temp = self._temp_sensor.get_outside_temp()
        self._heater_running = False
        self._fans_running = False

    def get_temp(self):
        return self._temp_sensor.get_outside_temp()

    def set_target_temp(self, input_target):
        AdminControl.set_target_temp(AdminControl, input_target)

    def get_target_temp(self):
        self._target_temp = AdminControl.get_target_temp(AdminControl)
        return self._target_temp

    def set_timer(self, input_time):
        self._total_seconds = AdminControl.set_timer(AdminControl,input_time)
        
    def get_timer(self):
        return AdminControl.get_timer(AdminControl)

    def toggle_fan(self):
        self._state = 1

    def toggle_heater(self):
        self._state = 4