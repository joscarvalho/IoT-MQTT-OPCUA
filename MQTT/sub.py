from paho.mqtt import client as mqtt_client
import random
import pyrebase #pip3 install pyrebase4

# MQTT Config
broker = 'localhost'
port = 1883
topic = "temperatura"
topic2 = "humidade"
client_id = 'PC'

# Firebase Config
firebase_config = {
    "apiKey": "...",
    "authDomain": "...",
    "databaseURL": "...",
    "storageBucket": "...",
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

def connect_mqtt():# -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)           
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic!")

        if msg.topic == "temperatura":
            data = {
                "Temperatura": float(msg.payload.decode())
            }

        if msg.topic == "humidade":
                data = {
                "Humidade": float(msg.payload.decode())
            }

        db.child("Samples").child("1").update(data)

    client.subscribe(topic)
    client.subscribe(topic2)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()            
