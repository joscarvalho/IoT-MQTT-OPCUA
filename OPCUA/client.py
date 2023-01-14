from opcua import Client
from time import sleep
import RPi.GPIO as GPIO
import dht11
import datetime

#initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#DHT-11 Pin
instance = dht11.DHT11(pin=23)

url = "opc.tcp://192.168.43.44:6000"

client = Client(url)

client.connect()
print("Client connected!")

while True:
        Temp = client.get_node("ns=2;i=2")
        Hum = client.get_node("ns=2;i=3")
        
        result = instance.read()

        if result.is_valid():
            print("Latest measurement: " + str(datetime.datatime.now()))

            temperatura = f'{result.temperature:-3.1f}'
            humidade = f'{result.humidity:-3.1f}'

        Temp.set_value(temperatura)
        Hum.set_value(humidade)
        sleep(2)