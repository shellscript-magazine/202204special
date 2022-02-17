#!/bin/env python3

import paho.mqtt.client as mqtt
import time

##
mqtt_topic = "confer/#"
csv_file = "./room1.csv"
subscriber_username = "sub1"
subscriber_password = "IBehie1h"
broker_hostname = "localhost"

##
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    now_unixtime = time.time()
    iot_device = msg.topic + "," + str(msg.payload, encoding='utf-8', errors='replace') + "," + str(now_unixtime)
    print(iot_device)
    with open(csv_file, mode='a') as f:
        f.write(iot_device + "\n")

##
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=subscriber_username, password=subscriber_password)
client.connect(broker_hostname)
client.loop_forever()
