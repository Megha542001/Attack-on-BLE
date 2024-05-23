import logging
import time

import Adafruit_BluefruitLE

# Enable debug output.
logging.basicConfig(level=logging.DEBUG)

# Define service and characteristic UUIDs used by the BLE module.
service_uuid = Adafruit_BluefruitLE.SERVICE_UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
rx_uuid      = Adafruit_BluefruitLE.CHAR_UUID_RX
tx_uuid      = Adafruit_BluefruitLE.CHAR_UUID_TX

# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()

# Initialize the BLE system.  MUST be called before other BLE calls!
ble.initialize()

# Start the BLE system.
ble.start_scan()

# Use the first BLE device found (the Arduino WiFi Rev2 board in this case).
device = ble.find_device(service_uuids=[service_uuid])

if device is None:
    raise RuntimeError('Failed to find BLE device!')

# Connect to the device.
device.connect()

# Get the BLE services offered by the device.
services = device.list_services()

# Find the BLE service and characteristics we want to use.
uart_service = None
rx_characteristic = None
tx_characteristic = None

for service in services:
    if service.uuid == service_uuid:
        uart_service = service
        break

if uart_service is None:
    raise RuntimeError('BLE UART service not found!')

for characteristic in uart_service.characteristics:
    if characteristic.uuid == rx_uuid:
        rx_characteristic = characteristic
    elif characteristic.uuid == tx_uuid:
        tx_characteristic = characteristic

if rx_characteristic is None or tx_characteristic is None:
    raise RuntimeError('BLE UART characteristics not found!')

# Turn on notification of RX characteristics using the callback above.
rx_characteristic.start_notify(rx_callback)

# Write a string to the TX characteristic.
tx_characteristic.write_value('Hello, world!')

# Wait for the message to be sent.
time.sleep(1)

# Disconnect from the device.
device.disconnect()

# Stop the BLE system.
ble.stop_scan()
ble.disconnect()
ble.uninitialize()
