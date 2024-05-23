from bleak import BleakScanner

async def discover_devices(name):
    devices = await BleakScanner.discover()
    print("Scanning for available BLE devices....")
    mydevice = None
    for d in devices:
        if d.name == name:
            mydevice = d
            print(dir(mydevice))
            break
    return mydevice



"""

async def connect_to_device(client):
    await asyncio.sleep(2)
    if client.is_connected:

        print("Connected to device.")
    else:
        print("Not connected to device.")

async def get_services(client):
    print("Services:")
    print(dir(client))
    services = await client.get_services()
    print("services loop...")
#    value = client.read_gatt_char("00002a00-0000-1000-8000-00805f9b34fb")
#    client.write_gatt_char("00002a00-0000-1000-8000-00805f9b34fb", b"new value")

        
    for service in services:
        print([services])
        print(service)
    char = await client.get_characteristic()
    print(f"Characteristic: {char}")
    print(f"UUID: {char.uuid}")
    print(f"Handle: {char.handle}")
    print(f"Properties: {char.properties}")
    data = await char.read()
    print(f"Data: {data}")
    return data



    service_uuids = []
    for svc in services:
        service_uuids.append([svc.uuid, svc.handle])
    import re
    vendor_specific_uuids = []
    for svc in services:
        if re.match(r"0000[0-9a-f]{4}-0000-1000-8000-00805f9b34fb", svc.uuid):
            vendor_specific_uuids.append(svc)
#    print(vendor_specific_uuids)
    for svc in service_uuids:
#       print(f"UUID: {svc[0]} Handle: {svc[1]}")
        await client.disconnect()


async def read_gatt_char(client, char_specifier=10):
    print(dir(client))
    

    char = await client.get_characteristic(char_specifier)
    print(f"Characteristic: {char}")
    print(f"UUID: {char.uuid}")
    print(f"Handle: {char.handle}")
    print(f"Properties: {char.properties}")
    data = await char.read()
    print(f"Data: {data}")
    return data

async def get_services_and_characteristics(client):
    services = await client.get_services()
    for svc in services:
        print(f"Service: {svc}")
        chars = await client.get_characteristics(svc)
        for char in chars:
            print(f" - Characteristic: {char}")


async def run():
    mydevice = await discover_devices()
    print(mydevice)
    if mydevice:
        print(f"Device_found\nName :{mydevice.name}\nMac add:{mydevice.address}")
        print("Connecting to...")
        async with BleakClient(mydevice.address) as client:
            await connect_to_device(client)
            await get_services(client)
#            await get_services_and_characteristics(client)
#            await read_gatt_char(client)

    else:
        print("Device not found.")

loop = asyncio.new_event_loop()
loop.run_until_complete(run())


"""