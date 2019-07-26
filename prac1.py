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
counter = 0

def main(channel):
	global counter
	GPIO.output(7,True)
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
			print("counter = ",counter)
			sleep(1)

	except KeyboardInterrupt:
		print("Exiting")
		#Turn off GPIOs
		GPIO.cleanup()
	except e:
		GPIO.cleanup()
		print("Some other error occured")
		print(e.message)
