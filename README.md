# Voice-control-LED_Strip

The MQTT service program provides an MQTT interface for controlling our 
APA102 LED strip by publishing MQTT messages to MQTT topics.


Circuit diagram:

![image](https://user-images.githubusercontent.com/115898447/196006075-2241e596-076e-4a12-8260-4356bd0a8e47.png)


We must have the Mosquitto MQTT broker service installed and running on our
Raspberry Pi, plus the Mosquitto MQTT clients tools.

Start the main.py script, as shown:
# Terminal 1
(venv) $ cd led_mqtt_service
(venv) $ python main.py

Open a second terminal and send an MQTT message using the following command:
# Terminal 2
$ mosquitto_pub -h "localhost" -t "led/lights/pattern" -m "red blue black"

Run the following command in Terminal 2 to make the LED strip animate:
# Terminal 2
$ mosquitto_pub -h "localhost" -t "led/lights/animation" -m "left"

