"""

Program entry point.

This program processes MQTT message for controlling APA102 LED Strip

Dependencies:
  pip3 install pigpio paho-mqtt luma.led_matrix

Built and tested with Python 3.7 on Raspberry Pi 4 Model B
"""
import logging
import config

from apa102 import APA102
from apa102_controller import APA102Controller



from mqtt_listener_client import MQTTListener

from signal import pause

logging.basicConfig(level=logging.INFO)

apa102 = APA102(num_leds=config.APA102_NUM_LEDS,
                port=config.APA102_PORT,
                device=config.APA102_DEVICE,
                bus_speed_hz=config.APA102_BUS_SPEED_HZ)


apa102.set_contrast(config.APA102_DEFAULT_CONTRAST)

apa102_controller = APA102Controller(apa102=apa102)





mqtt_listener = MQTTListener(config)
mqtt_listener.connect()

if __name__ == '__main__':

    try:
        pause()

    except KeyboardInterrupt:
        apa102.clear()
        
        mqtt_listener.disconnect()
        print("Bye")
