from paho.mqtt import client as mqtt_client
import random
import time
import RPi.GPIO as GPIO
import dht11
import datetime

#initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#DHT-11 Pin
instance = dht11.DHT11(pin=23)

#mosquitto -v -p 5000 -> Open mosquitto broker
broker = '192.168.43.44'
port = 1883
topic = "temperatura"
topic2 = "humidade"

client_id = 'raspberry'

def connect_mqtt():
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

def publish(client):
    time.sleep(0.5)
    while True:
        result = instance.read()

        if result.is_valid():
            print("Latest measurement: " + str(datetime.datatime.now()))

            temperatura = f'{result.temperature:-3.1f}'
            humidade = f'{result.humidity:-3.1f}'
            
            ret = client.publish(topic, temperatura)

            if ret[0] == 0:
                print(f"Sent '{temperatura}' to topic '{topic}' successfully!")
            else:
                print(f"Failed to send message to topic {topic}!")
    
            ret = client.publish(topic2, humidade)
            if ret[0] == 0:
                print(f"Sent '{humidade}' to topic '{topic2}' successfully!")
            else:
                print(f"Failed to send message to topic {topic2}!")

        time.sleep(5)   

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()