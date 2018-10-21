#!/usr/bin/env python3
#coding: utf-8
#

import json
import paho.mqtt.publish as mqtt_publish
import sys

class Temperature(object):
	ACQUIRE_FREQ = 30
	client = None

	#def __init__(self):
		#MQTT client initialization
		#self.client = mqtt_client.Client()
	#	self.client.on_connect = self.on_connect
	#	self.client.on_message = self.on_message

		#------
	#	self.client.connect('192.168.1.97',1883,60);
	#	self.client.loop_start();

	def sendData(self):
		"'sending temperatures '"
		#----
		jsonFrame = dict();
		jsonFrame['unitID'] = '02:00:c0:a8:00:10 | vm-dyn-0-209.siame.univ-tlse3.fr'
		jsonFrame['temperature'] = '10'

		#----
		mqtt_publish.single("1R1/014/temperature/command",json.dumps(jsonFrame),hostname="192.168.1.97")

#---
try:
	pub = Temperature()
	pub.sendData()
except (KeyboardInterrupt,SystemExit):
	print("\nbye")
	sys.exit(0)
	
	
