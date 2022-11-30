from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from time import sleep


running = True
adminPanel = AdminControl()
z1 = ZoneControl()
z2 = ZoneControl()
zonePanels = []

z1.set_target_temp(20)  # setting target temp to 12 deg

while running:
    z1.new_temperature_physics()
    print("Zone 1:")
    print("zone temp", z1.get_zone_temp())
    print("outside temp", z1.get_temp())
    print("target temp", z1.get_target_temp())
    print("zone state", z1.get_state())
    print("power consumed", z1.get_power_consumed())
    sleep(1)
