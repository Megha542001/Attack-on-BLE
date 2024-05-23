import bluetooth

# Replace with the MAC address of your target device
target_mac_address = "DC:E8:2B:A8:CC:84"

try:
    # Discover nearby Bluetooth devices
    nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=10, flush_cache=True, lookup_class=False)

    for addr, name in nearby_devices:
        if addr == target_mac_address:
            print(f"Connecting to {name} ({addr})")

            # Establish a connection to the target device
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((addr, 1))

            # Now, you can send and receive data through 'sock'
            # For example, to send data:
            sock.send("Hello, Bluetooth!")

            # To receive data (adjust buffer size as needed):
            data = sock.recv(1024)
            print(f"Received data: {data.decode('utf-8')}")

            # Close the Bluetooth socket when done
            sock.close()
            break
    else:
        print("Device not found in the nearby devices.")

except bluetooth.BluetoothError as e:
    print(f"Bluetooth error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
