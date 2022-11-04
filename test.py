from adminControlPanel import adminControl
from zoneControlPanel import zoneControl
from tempSensor import tempSensor

running = True
adminPanel = adminControl()
z1 = zoneControl()
z2 = zoneControl()
zonePanels = []

while running:
    print(z1.get_temp())