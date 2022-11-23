from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from time import sleep
import asyncio


running = True
adminPanel = AdminControl()
z1 = ZoneControl()
z2 = ZoneControl()
zonePanels = []

z1.set_target_temp(20)  # setting target temp to 12 deg

while running:
    # print("Zone 1 Temp: ", z1.get_temp())  # Prints a string
    # print("Average Temp:", adminPanel.avg_temp())  # Prints an int
    # asyncio.run(z1.temperature_physics())  # calling temperature_physics function
    z1.new_temperature_physics()
    print("Zone 1:")
    print("zone temp", z1.get_zone_temp())
    print("outside temp", z1.get_temp())
    print("target temp", z1.get_target_temp())
    print("zone state", z1.get_state())
    sleep(1)
