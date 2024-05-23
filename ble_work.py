import time
import pygatt

# Define the Bluetooth address of your Arduino
arduino_address = "84:CC:A8:2B:E8:DE"

# Define the UUID of the characteristic you want to interact with
characteristic_uuid = "19B10001-E8F2-537E-4F6C-D104768A1214"

def handle_data(handle, value_bytes):
    received_message = value_bytes.decode('utf-8')
    print("Received message from Arduino:", received_message)

def main():
    adapter = pygatt.GATTToolBackend()

    try:
        adapter.start()
        device = adapter.connect(arduino_address)

        device.subscribe(characteristic_uuid, callback=handle_data)

        while True:
            message_to_send = "Hello, Arduino!"
            device.char_write(characteristic_uuid, message_to_send.encode('utf-8'))
            time.sleep(1)  # Send message every second

    except KeyboardInterrupt:
        pass
    finally:
        adapter.stop()

if __name__ == "__main__":
    main()
