from ast import If
import asyncio
import sys
from bleak import BleakScanner, BleakClient
from bleak.backends.bluezdbus.client import BleakClientBlueZDBus
import struct
import json
from time import sleep
from random import uniform
from datetime import datetime
import getpass

async def run():
    client = None
    device = await BleakScanner.find_device_by_filter(
        lambda d, ad: d.name and d.name.lower() == device_name.lower()
    )
    if device is None:
        print("{} not found".format(device_name))
        sys.exit()
    else:
        print("{} found".format(device))
    valid = False
    async with BleakClient(device) as client:
        while client.is_connected:
            if valid == False:
                input_str = getpass.getpass()
                bytes_to_send = input_str.encode()
                await client.write_gatt_char(passwordChar, bytes_to_send)
                await asyncio.sleep(1)
                aa = await client.read_gatt_char(passwordChar)

                if bytearray(b'\x01\x00') == aa:
                    valid = True
                    print('welcome admin !!')
                else:
                    print('wrong password :/ !!')
                    valid = False

            elif valid == True:
                await client.start_notify(dataChar, notification_handler)

            await asyncio.sleep(1)


device_name = "Station"
dataChar = "d508bc0a-ecdd-5ba5-9d33-13d5887a7718"
passwordChar = "7dfe60ef-175f-5a61-ac33-8a658b07cdb7"

loop = asyncio.get_event_loop()
loop.run_until_complete(run())