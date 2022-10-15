# IoTLED MQTT Service

The following is a list of MQTT topic and message formats recognise by the led MQTT Service.

## Clear (turn off) all LEDS on APA102 LED Strip

 * MQTT Topic: `led/lights/clear`
 * MQTT Message Format: Pass an empty message

*Example:*

`mosquitto_pub -h "localhost" -t "led/lights/clear" -m ""`

---

## Push color(s) into the APA102 LED Strip

 * MQTT Topic: `led/lights/push`
 * MQTT Message Format: Space separated list of colour names or hex values

*Example:*

`mosquitto_pub -h "localhost" -t "led/lights/push" -m "red blue black"`

---

## Set Repeating Color Pattern on the APA102 LED Strip

 * MQTT Topic: `led/lights/pattern`
 * MQTT Message Format: Space separated list of colour names or hex values

*Example:*

`mosquitto_pub -h "localhost" -t "led/lights/pattern" -m "red blue black"`

---

## Set LED Contrast

 * MQTT Topic: `led/lights/contrast`
 * MQTT Message Format: A number between `0` and `255`

*Example:*

`mosquitto_pub -h "localhost" -t "led/lights/contrast" -m "128"`

---

## Set LED Animation Mode


 * MQTT Topic: `led/lights/animation`
 * MQTT Message Format: One of the following values:
    * stop
    * left
    * right
    * blink
    * rainbow

*Example:*

`mosquitto_pub -h "localhost" -t "led/lights/animation" -m "blink"`

---

## Set LED Animation Speed


 * MQTT Topic: `led/lights/speed`
 * MQTT Message Format: A number between `1` and `10`

*Example:*

`mosquitto_pub -h "localhost" -t "led/lights/speed" -m "10"`

---


