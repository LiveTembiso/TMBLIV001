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

def main(channel):
	global counter
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
			leds = format(counter,"03b")
			GPIO.output(7,int(leds[0]))
			GPIO.output(13,int(leds[1]))
			GPIO.output(15,int(leds[2]))
			print(leds)
			sleep(1)

	except KeyboardInterrupt:
		print("Exiting")
		#Turn off GPIOs
		GPIO.cleanup()
	except e:
		GPIO.cleanup()
		print("Some other error occured")
		print(e.message)
