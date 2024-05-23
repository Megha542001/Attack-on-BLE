import bluetooth
print('Device scanning...')

nearby_devices = bluetooth.discover_devices(
    lookup_names=True,
    flush_cache=True,
    duration=30
    )

for addr,name in nearby_devices:
    print("%s - %s" % (addr,name))

    #for services in bluetooth.find_service(address = addr):
        #print('Name: ', (services['name']))
        #print('protocal: ',(services['protocol']))