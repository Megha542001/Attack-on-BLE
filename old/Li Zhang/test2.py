import bluetooth
from bluetooth.ble import DiscoveryService

services= DiscoveryService()
devices = services.discover(2)

for add,name in devices,items():
    print("name: {},add: {}".format(name,add))