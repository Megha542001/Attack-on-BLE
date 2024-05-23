import asyncio
import discover, connect, service

async def run():
    mydevice = await discover.discover_devices("Test")
    if mydevice:
        print(f"Device_found\nName :{mydevice.name}\nMac add:{mydevice.address}")
        print("Connecting to...")
        print("Device details :",mydevice.details)
        print("Meta data :",mydevice.metadata)
        
        
        client = await connect.connect_to_device(mydevice)
        if client == None:
            exit
        await connect.my_service(mydevice) 
    else:
        print("Device not found.")

loop = asyncio.new_event_loop()
loop.run_until_complete(run())
