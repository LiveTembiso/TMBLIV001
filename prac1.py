#!/usr/bin/python3
"""
Name: Tembiso Live
Student Number: TMBLIV001
Prac: 1
Date: 25th July 2019

"""

import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED

led = LED(7)

def main():
	print("Hello world")
	led.on()
	sleep(2)
	led.off()
	sleep(2)

if __name__ == "__main__":
	#GPIO stopped correctly
	try:
		while True:
			main()
	except KeyboardInterrupt:
		print("Exiting")
		#Turn off GPIOs
		GPIO.cleanup()
	except e:
		GPIO.cleanup()
		print("Some error occured")
		print(e.message)
