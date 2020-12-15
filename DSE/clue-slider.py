"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython
Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt
import ast

def display_text(value):
   clue_data[0].text = "Accel: {} {} {} m/s^2".format(*value["accelerometer"])
    clue_data[1].text = "Gyro: {} {} {} dps".format(*value["gyro"])
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*value["magnetometer"])
    clue_data[3].text = "Pressure: {} hPa".format(value["pressure"])
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {} C".format(value["temperature"])
    clue_data[6].text = "Humidity: {} %".format(value["humidity"])
    clue_data[7].text = "Proximity: {}".format(clue.proximity)
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(*value["color"])
    clue_data.show()


clueValue = {
    'accelerometer': (0,0,0),
    'gyro': (0,0,0),
    'temperature': 0,
    'pressure': 1013,
    'magnetometer': (0,0,0),
    'humidity':0,
    'proximity': 0,
    'color': (0,0,0,0)
}



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("slider-clue")
        display_text(clueValue)
        

def on_message(client, userdata, msg):
    # display_text(int(msg.payload.decode()))
    slider_value = ast.literal_eval(msg.payload.decode())
    clueValue["accelerometer"] = (int(slider_value["accelerometer_x"]), int(slider_value["accelerometer_y"]), int(slider_value["accelerometer_z"]))
    clueValue["gyro"] = (int(slider_value["gyro_x"]), int(slider_value["gyro_y"]), int(slider_value["gyro_z"]))
    clueValue["temperature"] = int(slider_value["temperature"])
    clueValue["pressure"] = int(slider_value["pressure"])
    clueValue["magnetometer"] = (int(slider_value["magnetic_x"]), int(slider_value["magnetic_y"]), int(slider_value["magnetic_z"]))
    clueValue["humidity"] = int(slider_value["humidity"]),
    clueValue["proximity"] = int(slider_value["proximity"]),
    clueValue["color"] = (int(slider_value["color_r"]), int(slider_value["color_g"]), int(slider_value["color_b"]),int(slider_value["color_c"]))
  
    display_text(clueValue)

# clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()