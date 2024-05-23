#include <ArduinoBLE.h>

const int ledPin = 13;
bool isBluetoothConnected = false;

BLEService chatService("19B10000-E8F2-537E-4F6C-D104768A1214");
BLEStringCharacteristic chatCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", BLEWrite | BLENotify, 200);

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);

  while (!BLE.begin()) {
    Serial.println("Starting BLE failed! Retrying...");
    delay(1000);
  }

  BLE.setLocalName("Arduino_BLE");
  BLE.setAdvertisedService(chatService);
  chatService.addCharacteristic(chatCharacteristic);
  BLE.addService(chatService);
  chatCharacteristic.setValue("Hello, Raspberry Pi!");

  while (true) {
    BLE.advertise();
    Serial.println("BLE peripheral is running. Waiting for connections...");

    BLEDevice central = BLE.central();

    if (central) {
      Serial.print("Connected to central: ");
      Serial.println(central.address());
      digitalWrite(ledPin, HIGH);
      isBluetoothConnected = true;

      while (central.connected()) {
        if (chatCharacteristic.written()) {
          String receivedMessage = chatCharacteristic.value();
          Serial.println("Received message: " + receivedMessage);
          // You can add your logic here to respond to the message if needed.
          chatCharacteristic.setValue("Message received: " + receivedMessage);
        }
      }

      Serial.print("Disconnected from central: ");
      Serial.println(central.address());
      digitalWrite(ledPin, LOW);
      isBluetoothConnected = false;
    }

    if (!isBluetoothConnected) {
      digitalWrite(ledPin, HIGH);
      delay(500);
      digitalWrite(ledPin, LOW);
      delay(500);
    }
  }
}

void loop() {
  // Your main loop code, if any, can go here.
}
