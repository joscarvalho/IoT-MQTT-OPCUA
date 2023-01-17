from opcua import Server
import time
import pyrebase

server = Server()

url = "opc.tcp://192.168.43.44:6000"
server.set_endpoint(url)

name = "PFFT"

addspace = server.register_namespace(name)

node = server.get_objects_node()
print(f"NODE : {node}")

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Hum = Param. add_variable(addspace, "Humidity", 0)

Temp.set_writable()
Hum.set_writable()

# Firebase Config
firebase_config = {
    "apiKey": "...",
    "authDomain": "...",
    "databaseURL": "...",
    "storageBucket": "...",
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


server.start()
print(f"Server started at '{url}'")

def run():
    while True:
        temperature = Temp.get_value()
        humidity = Hum.get_value()
        print(f"Temp: '{temperature}' Humidity: '{humidity}'")
        data = {
            "Temperatura": float(temperature),
            "Humidade": float(humidity)
        }
        db.child("Samples").child("1").update(data)

        time.sleep(2)

if __name__ == "__main__":
    run()
