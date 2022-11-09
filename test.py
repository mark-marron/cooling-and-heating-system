from adminControlPanel import AdminControl
from zoneControlPanel import ZoneControl
from TempSensor import TempSensor


running = True
adminPanel = AdminControl()
z1 = ZoneControl()
z2 = ZoneControl()
zonePanels = []

while running:
    print(z1.get_temp())
