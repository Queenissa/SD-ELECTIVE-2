from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        cp.red_led = True
        client.subscribe("switch-control")

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "slider1Enabled":
        cp.pixels[0] = (255, 255, 255)

    elif msg.payload.decode() == "slider1Disabled":
        cp.pixels[0] = (0,0,0)

    elif msg.payload.decode() == "slider2Enabled":
        cp.pixels[1] = (255,255,255)

    elif msg.payload.decode() == "slider2Disabled":
        cp.pixels[1] = (0,0,0)

    elif msg.payload.decode() == "slider3Enabled":
        cp.pixels[2] = (255,255,255)
        
    elif msg.payload.decode() == "slider3Disabled":
        cp.pixels[2] = (0,0,0)


cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt