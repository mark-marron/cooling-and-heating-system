from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from TempSensor import TempSensor


running = True
adminPanel = AdminControl()
z1 = ZoneControl()
z2 = ZoneControl()
zonePanels = []

while running:
    print("Zone 1 Temp: ", z1.get_temp())  # Prints a string
    print("Average Temp:", adminPanel.avg_temp())  # Prints an int
