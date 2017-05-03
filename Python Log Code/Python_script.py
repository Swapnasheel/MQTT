'''
Author: Swapnasheel
EE281 Project

This script when started on Raspberry Pi, activates the MQTT services making it the Broker and waiting for client messages.

'''
import paho.mqtt.client as mqtt
import datetime
import os
import time
import logging 
import string
import sys

onstarttime = 0
Mylogger = None

Mylogger = logging.getLogger(__name__)
Mylogger.setLevel(logging.INFO)

#time handler

timeformat = "%a %b %c %y %h.%m.%s"
today = datetime.datetime.today()
timestamp = today.strftime(timeformat)
my_logfile = 'logs/logs' + timestamp + '.log'
handler = logging.FileHandler(my_logfile)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(time)s - %(levelname)s - %(message)s ')
#logging.info('\n')
handler.setFormatter(formatter)

Mylogger.addHandler(handler)

    
    
def on_message(mqttc, obj, msg):
    
    global onstarttime
    global Mylogger
    
    localtime = time.asctime(time.localtime(time.time()))
    
    print ("Your Switch Status " + " - " + msg.payload)
    
    if (msg.topic == "MQTT/switch"):
        if (msg.payload == 'switch1_ON' or msg.payload == 'switch2_ON' or msg.payload == 'switch3_ON' or msg.payload == 'switch4_ON'):
            onstarttime = time.time()
            
            logmessage = "Light turned on at " + localtime
            print (logmessage)
            Mylogger.info(logmessage)
            
        elif (msg.payload == 'switch1_OFF' or msg.payload == 'switch2_OFF' or msg.payload == 'switch3_OFF' or msg.payload == 'switch4_OFF'):
            runtime = time.time() - onstarttime
   			
            logmessage = "Light turned off at " + localtime
            print (logmessage)
            Mylogger.info(logmessage)
            
            #total time
            logmessage = "The Light was on for total " + str(int(runtime)) + " sec"
            print (logmessage)
            Mylogger.info(logmessage)

			
			

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect("192.168.0.41",1883,60)
mqttc.subscribe("MQTT/switch", 2)
mqttc.loop_start()
#mqttc.loop_forever()
while(True):
	time.sleep(1)
    
			