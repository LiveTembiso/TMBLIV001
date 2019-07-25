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

def main():
	print("Hello world")
	GPIO.output(7,True)
	sleep(2)
	GPIO.output(7,False)
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
		print("Some other error occured")
		print(e.message)
