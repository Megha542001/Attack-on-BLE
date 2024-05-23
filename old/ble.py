import asyncio
from bleak import BleakScanner,BleakClient

target_addr = ""
heart_uuid = "8158b2fd-94e4-4ff5-a99d-9a7980e998d7"

async def main():
    global target_addr
    devices = await BleakScanner.discover()
    for d in devices:
        if d.rssi > -70:
            print(d, d.rssi)

        if heart_uuid in d.metadata['uuids']:
            target_addr = d.address
            print("heart rate device addr:", target_addr)
                
    print('---------------------------------------------------')
    if target_addr != "":
        async with BleakClient(target_addr) as client:
            print(f"Connected: {client.is_connected}")
            svcs = await client.get_services()
            print(dir(svcs))
            print("Services:")
            for service in svcs:
                print(service)
                for char in service.characteristics:
                    print(char)           
            
if __name__ == "__main__":
    asyncio.run(main())
