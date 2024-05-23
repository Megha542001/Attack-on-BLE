import bluetooth

target_name = "Arduino_BLE"
target_address = None

nearby_devices = bluetooth.discover_devices(duration=10, lookup_names=True, flush_cache=True, lookup_class=True)

for addr, name, _ in nearby_devices:
    if target_name == name:
        target_address = addr
        break

if target_address is not None:
    print("Found target device with address:", target_address)
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_address, 1))
    print("Connected to Arduino_BLE")

    while True:
        message = input("Enter a message to send to Arduino_BLE: ")
        sock.send(message)

    sock.close()
else:
    print("Target device not found.")
