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

#Increases counter when button(pin 11) is pressed
def increment(channel):
	print("Increment")
	if counter < 7:
		counter += 1
	elif counter == 7:
		counter = 0
	GPIO.output(7,True)
	sleep(1)

#Decreases couunter when button(pin 12) is pressed
def decrement(channel):
	print("Decrement")
	if counter > 0:
		counter -= 1
	elif counter == 0:
		counter = 7
	GPIO.output(7,True)
	sleep(1)

GPIO.add_event_detect(11,GPIO.FALLING,callback=increment,bouncetime=300)
GPIO.add_event_detect(12,GPIO.FALLING,callback=decrement,bouncetime=300)

#if __name__ == "__main__":
	#GPIO stopped correctly
try:
	while True:
		#main()
		print("Counter = ", counter)
		sleep(1)
except KeyboardInterrupt:
	print("Exiting")
	#Turn off GPIOs
	GPIO.cleanup()
except e:
	GPIO.cleanup()
	print("Some other error occured")
	print(e.message)
