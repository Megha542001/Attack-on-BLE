import asyncio
from bleak import BleakScanner,BleakClient
import platform


# target_addr = "7C:9E:BD:3B:50:7A"
target_addr = ""
heart_uuid = "46871e12-86a9-4704-823e-6389de122daf"
#heart_uuid = "0000fff0-0000-1000-8000-00805f9b34fb"

async def main():
    global target_addr
    devices = await BleakScanner.discover()
    for d in devices:
        if d.rssi > -70:
            print(d, d.rssi,d.metadata)

        if heart_uuid in d.metadata['uuids']:
            target_addr = d.address
            print("heart rate device addr:", target_addr)
                
    print('---------------------------------------------------')
    if target_addr != "":
        async with BleakClient(target_addr) as client:
            print(f"Connected: {client.is_connected}")
            svcs = await client.get_services()
            print("Services:",svcs)
            for service in svcs:
                print(service)
                for char in service.characteristics:
                    print(char) 
                        
if __name__ == "__main__":
    asyncio.run(main())

