#Quency Atacador


from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        cp.red_led = True
        client.subscribe("neopixelSwitch")

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "enabled1":
        cp.pixels[0] = (255, 255, 255)

    elif msg.payload.decode() == "disabled1":
        cp.pixels[0] = (0,0,0)
    
    elif msg.payload.decode() == "enabled1":
        cp.pixels[1] = (255, 255, 255)

    elif msg.payload.decode() == "disabled1":
        cp.pixels[1] = (0,0,0)







    
       


cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()
