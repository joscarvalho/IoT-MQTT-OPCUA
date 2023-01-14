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
    "apiKey": "AIzaSyBWn6HM7DSLfYc8_FYws8HdM7qPp0ysYb4",
    "authDomain": "projeto-di-76003.firebaseapp.com",
    "databaseURL": "https://projeto-di-76003-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "projeto-di-76003.appspot.com",
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