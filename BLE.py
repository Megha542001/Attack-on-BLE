import time
import random
import pygatt

# Replace with the MAC address of the Arduino receiver
receiver_mac_address = "DC:E8:2B:A8:CC:84"

# Generate a random string
def generate_random_string(length=10):
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(charset) for _ in range(length))

# Callback function when notifications are received
def handle_data(handle, value_bytes):
    received_message = value_bytes.decode('utf-8')
    print(f"Received: {received_message}")

# Create a BLE adapter
adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect(receiver_mac_address)

    # Enable notifications for the characteristic
    device.subscribe("19b10001-e8f2-537e-4f6c-d104768a1214", callback=handle_data)

    while True:
        random_message = generate_random_string()
        print(f"Sending: {random_message}")
        device.char_write("19b10001-e8f2-537e-4f6c-d104768a1214", random_message.encode('utf-8'))
        time.sleep(2)  # Send a new message every 2 seconds

finally:
    adapter.stop()
