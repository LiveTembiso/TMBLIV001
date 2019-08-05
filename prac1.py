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

counter = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

def increment(channel):
#Check if the increment button was pressed
	global counter
	if counter < 7:		#Check that counter is not equal to 7
		counter += 1
	else:
		counter = 0     #if counter = 7 set it to 0
	setup()

def decrement(channel):
	global counter
	if counter > 0:         #check if counter = 0
		counter -= 1	#if not add 1 to counter
	else:
		counter = 7	#if counter = 0 set counter to 7
	setup()

def setup():
	leds = format(counter,"03b")   #Converts counter into a 3 bit binary number
	GPIO.output(7,int(leds[0])) #takes 1st bit of the binary number and passes it to pin 13 if it's 0 light goes off if 1 goes on
	GPIO.output(13,int(leds[1])) #takes 2nd bit of binary number and passes it to led in pin 13 ...
	GPIO.output(15,int(leds[2])) #takes 3rd bit of binary number and assigns it to the led in pin 15
	print(leds) #print binary number to screen

GPIO.add_event_detect(11,GPIO.FALLING,callback=increment,bouncetime=300) #Calls main when button in pin11 is pressed
GPIO.add_event_detect(12,GPIO.FALLING,callback=decrement,bouncetime=300) #Calls main when button connected to GPIO pin 12 is pressed

def main():
	pass

if __name__ == "__main__":
	try:
		while(True):
			main()
	except KeyboardInterrupt:
		GPIO.cleanup()
