# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

# magnet = 35 # gnd = 34

class Magnet:
    gpin = 0

    def __init__(self, pin=35):
        self.gpin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpin, GPIO.OUT)
        GPIO.output(self.gpin, 0)
        # print("__magnet init__")

    def __del__(self):
        GPIO.output(self.gpin, 0)
        GPIO.cleanup()
        # print "__deleted__"

    def up(self):
        GPIO.output(self.gpin, 1)

    def down(self):
        GPIO.output(self.gpin, 0)
