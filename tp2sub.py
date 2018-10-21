#!/usr/bin/env python3
#coding: utf-8
#

import json
import paho.mqtt.client as mqtt_client
import sys

class Temperature(object):
	ACQUIRE_FREQ = 30
	client = None

	def __init__(self):
		#MQTT client initialization
		self.client = mqtt_client.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message

		#------
		self.client.connect("192.168.1.97",1883,60);
		self.client.loop_start();

	def on_connect(self,client,userdata,flags,rc):
		if(rc != 0):
			return
		self.client.subscribe("1R1/014/temperature/command")
		#------

	def on_message(self,client,userdata,msg):
		
		"""if msg.topic != self._command_topic:
			#this module is not concerned by this message, returning
			log.debug("received a message not for me on" + msg.topic)
			print("perdu\n")
			return"""
		try:
			#loading and verifying payload
			msg.payload = json.loads(msg.payload.decode('utf-8'))
			print(str(msg.payload))
		except Exception as ex:
			print("perdu excp json\n")
			log.error("exception handling json payload:" + str(ex))
			return
		"""else:
			#executed if no exception arise
			print("perdu\n")
			if payload['dest'] != "all" and payload['dest'] != str(self.unitID):
				return
		"""

try:
	temp = Temperature()

	temp.client.loop_forever()

except (KeyboardInterrupt,SystemExit):
	print("\nbye")
	sys.exit(0)
	
	 
