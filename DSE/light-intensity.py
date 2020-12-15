from microbit import *
import paho.mqtt.client as mqtt


 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("lightIntensity")
        display.show(Image.YES)

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if
    
    



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()