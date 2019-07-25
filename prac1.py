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

def main():
	button_state = GPIO.input(23)
	if button_state == False:
		print("Hello world")
		GPIO.output(7,True)
		sleep(2)
		GPIO.output(7,False)
		sleep(2)
	else:
		GPIO.output(24,False)

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
