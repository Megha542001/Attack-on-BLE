from sense_hat import SenseHat
import pyrebase
import time
import calendar
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


#Broker = "192.168.66.251"              #Enter your broker IP Address

""" MQTT config values """

Broker = "192.168.66.251" # Enter broker IP Address
port = 1888 # Enter port number eg 1888
topic = "arduino/data"        #Enter your broker TOPIC 
sub_topic = "sensor/instructions"    # receive messages on this TOPIC
output = ""

""" Firebse database config values """

db_config = {
    "apiKey": "azKNMjOIhOEG1bks4rk6ann4T3JsZTJuOOupPQ38",
    "authDomain": "iot2023-6ff42.firebaseapp.com",
    "databaseURL": "https://iot2023-6ff42-default-rtdb.europe-west1.firebasedatabase.app/",
    "projectId": "iot2023-6ff42",
    "storageBucket": "iot2023-6ff42.appspot.com"
  };


def on_connect(client, userdata, flags, rc):
    client.subscribe("arduino/data")

        


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))
    

def on_message(client, userdata, msg):
        message = msg.payload
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

firebase = pyrebase.initialize_app(db_config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("—————————————-")
print()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1888, 60)
client.loop_start()


while True:
        
            print(output)
            lst = output.split(";")
            print(lst)
            client.publish("pi/upload", output)
        
        
        
data = {
    "DateTime": output[0],
    "Humidity": output[1],
    "RoomTemp": output[2]
    }

db.child("Sensor").child("1-set").set(data)
db.child("Sensor").child("2-set").set(data)
db.child("Sensor").child("3-push").push(data)

time.sleep(5)


