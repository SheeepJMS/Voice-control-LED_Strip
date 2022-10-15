#IoT Voice-controlled LED via MQTT 


* `requirements.txt` - Python dependencies required for this chapter

  
* `led_mqtt_service`
  * `README.md` - IoTree MQTT Topic and Message Format Documentation and Examples
  * `main.py` - Main program
  * `config.py` - Program Configuration
  * `apa102.py` - APA102 LED Strip Electronic Interface 
  * `apa102_controller.py` - Interprets PubSub messages to control APA102 LED Strip 
  * `mqtt_listener.py` - MQTT Client. Subscribes to MQTT Topic and republishes MQTT messages as PubSub messages
 