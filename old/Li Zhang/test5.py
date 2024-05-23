import time
from bluetooth import *

alreadyFound = []

def findDevs():
    foundDevs = discover_devices(lookup_names=True)
    for (addr,name) in foundDevs:
        print("Bluetooth device:"+str(name))
        print("Bluetooth Mac:"+str(addr))
        alreadyFound.append(addr)
        
while True:
    findDevs()
    time.sleep(10)