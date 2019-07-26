#!/usr/bin/python3
"""
Name: Tembiso Live
Student Number: TMBLIV001
Prac: 1
Date: 25th July 2019

"""

import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
counter = 0
bulb = ""

def main(channel):
	global counter
	#global bulb = format(counter,'05b')
	GPIO.output(7,1)
	GPIO.output(13,1)
	GPIO.output(15,1)
	if channel == 11:
		if counter < 7:
			counter += 1
		else:
			counter = 0

	else:
		if counter > 0:
			counter -= 1
		else:
			counter = 7

	

GPIO.add_event_detect(11,GPIO.FALLING,callback=main,bouncetime=300)
GPIO.add_event_detect(12,GPIO.FALLING,callback=main,bouncetime=300)

if __name__ == "__main__":
	#GPIO stopped correctly
	try:
		while True:
			GPIO.output(7,False)
			GPIO.output(13,0)
			GPIO.output(15,0)
			print(format(counter,'03b'))
			sleep(1)
	except KeyboardInterrupt:
		print("Exiting")
		#Turn off GPIOs
		GPIO.cleanup()
	except e:
		GPIO.cleanup()
		print("Some other error occured")
		print(e.message)
