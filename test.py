from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from time import sleep


running = True
adminPanel = AdminControl()
z1 = ZoneControl()
z2 = ZoneControl()
zonePanels = []
z1.temperature_physics()  # calling temperature_physics function
z1.set_target_temp(12)  # setting target temp to 12 deg

while running:
    # print("Zone 1 Temp: ", z1.get_temp())  # Prints a string
    # print("Average Temp:", adminPanel.avg_temp())  # Prints an int
    print("Zone 1:")
    print(z1.get_zone_temp())
    print(z1.get_state())
    sleep(5)
