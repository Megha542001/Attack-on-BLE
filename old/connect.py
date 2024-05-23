import asyncio
from bleak import BleakClient

async def connect_to_device(device):
    client = BleakClient(device.address)
#    print(dir(device.name))
#    print(dir(device.rssi))
    await asyncio.sleep(2)
    print(dir(client))

    services = client.services
    print(dir(services))
    for service in services:
        characteristics = service.get_characteristics()
        for characteristic in characteristics:
            value = characteristic.read_gatt_char()
            print(f"Characteristic {characteristic.uuid} has value {value}")


    if client.is_connected:
            print("Connected to device.")
            return client
    else:
            return None

async def read_temperature(address):
        data = address.metadata
        async with BleakClient(address) as client:
            temperature_uuid = data['uuids']
            temperature_data = await client.read_gatt_char(temperature_uuid)
            return temperature_data

async def my_service(mydevice):
            data = mydevice.metadata
            adv = mydevice.details[0]
            scan = mydevice.details[1]
            print("UUIDs:", data['uuids'])
            print("Manufacturer data:", data['manufacturer_data'])


"""
    # Discover characteristics
            characteristics = await client.discover_characteristics()
            # Iterate over the characteristics and get their UUIDs
            for characteristic in characteristics:
                uuid = characteristic.uuid
                # Read data from the characteristic
                data = await client.read_gatt_char(uuid)
                print(f"UUID: {uuid} Data: {data}")
"""
