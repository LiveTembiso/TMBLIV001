#!/usr/bin/python3
"""
Name: Tembiso Live
Student Number: TMBLIV001
Prac: 1
Date: 25th July 2019

"""

import RPi.GPIO as GPIO


def main():
	print("Hello world")

if __name__== "__main__":
	#GPIO stopped correctly
	try:
		while True:
			main()
	except KeyboardInterrupt:
		print("Exitting")
		#Turn off GPIOs
		GPIO.cleanup()
	except e:
		GPIO.cleanup()
		print("Some error occured")
		print(e.message)
