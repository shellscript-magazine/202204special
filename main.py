import time
import dht
from machine import Pin
from umqtt.simple import MQTTClient

mqtt_topic = "confer/room1"
publisher_username = "pub1"
publisher_password = "パスワード"
publisher_id = "room1_esp32"
broker_address = "192.168.1.100"
interval_time = "1"

hf_sensor = Pin(5, Pin.IN, Pin.PULL_UP)
th_sensor = dht.DHT11(Pin(22))

time.sleep(5)

while True:
  value1 = hf_sensor.value()
  th_sensor.measure()
  value2 = th_sensor.temperature()
  value3 = th_sensor.humidity()
  iot_value = str(value1)+","+str(value2)+","+str(value3)
  print(iot_value)
  publisher = MQTTClient(publisher_id,broker_address,user=publisher_username,password=publisher_password)
  publisher.connect()
  publisher.publish(mqtt_topic, msg=iot_value)
  publisher.disconnect()
  time.sleep(int(interval_time))