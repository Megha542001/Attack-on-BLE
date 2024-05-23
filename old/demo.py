import pyrebase
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from datetime import datetime
import time
import calendar


""" Data """

datafield_names = ["DateTime", "Humidity","RoomTemp"]



""" Firebse database config values """


db_config = {
    "apiKey": "azKNMjOIhOEG1bks4rk6ann4T3JsZTJuOOupPQ38",                                            #Enter your Firebase API-KEY
    "authDomain": "iot2023-6ff42.firebaseapp.com",                                               #Enter your project authentication domain
    "databaseURL": "https://iot2023-6ff42-default-rtdb.europe-west1.firebasedatabase.app",       #Enter your project database URL
    "projectId": "iot2023-6ff42",                                                                #Enter your project unique ID
    "storageBucket": "iot2023-6ff42.appspot.com",                                                #Enter your Storage Bucket ID
                                                                                                #Enter API ID
    

};


""" MQTT config values """

broker = "192.168.157.251" # Enter broker IP Address
port = 1888 # Enter port number eg 1888
topic = "arduino/data"        #Enter your broker TOPIC 



""" Pi MQTT Broker methods setup """

# When connected to MQTT Broker
def on_connect(client, userdata, flags, rc):
    print("Connected to broker at {} port {}".format(broker, port))
    client.subscribe(topic)
    print("Subscribed to:", topic)

# When disconnected from MQTT Broker
def on_disconnect(client, userdata, rc):
    if rc == 0:
        print("Disconnected from broker at {} port {}".format(broker, port))
    else:
        print("Unexpected disconnection.")


# When receiving an MQTT message
def on_message(client, userdata, msg):
    message_in = msg.payload.decode("utf-8")
    topic = msg.topic

    # Only run if the message is data from the fixed platform
    if topic == "arduino/data":
        
        curr_unixtime = calendar.timegm(time.gmtime())
        curr_time = datetime.fromtimestamp(curr_unixtime)\
                    .strftime("%Y-%m-%d %H:%M:%S")
        print("Data received on topic '{}' at {}:".format(msg.topic, curr_time))
        print(message_in)
        
        # Add timestamp in seconds
        message = str(curr_unixtime) + ";" + message_in
        
        data = message.split(";")
        #print(data)

        # Send sensor data and timestamp to
        # Firebase Realtime database (one at a time)
        for i in range(3):
            database.child(datafield_names[i])
            output = {"Sensor": data[i]}
            database.set(output)


# When publishing an MQTT message
def on_publish(client, userdata, mid):
    print('Data published to broker with mid {}'.format(mid))       


""" Execution """

def main():    
    try:
        # Connect to Pi MQTT Broker
        PiClient.connect(broker, port, 60)
        PiClient.loop_start()

        # Keep the broker running
        while True:
            time.sleep(10)
            
    # Exit script on ^C
    except KeyboardInterrupt:
        print("\nExit with ^C")
        PiClient.disconnect()
        PiClient.loop_stop()
        pass
  

if __name__ == "__main__":        

    firebase = pyrebase.initialize_app(db_config)
    storage = firebase.storage()
    database = firebase.database()

    PiClient = mqtt.Client()
    PiClient.on_connect = on_connect
    PiClient.on_disconnect = on_disconnect
    PiClient.on_message = on_message
    PiClient.on_publish = on_publish
    
    main()
