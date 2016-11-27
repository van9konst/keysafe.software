# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import constants
import time

# magnet = 35 # gnd = 34

class Magnet:
    gpin = 0

    def __init__(self, pin=10):
        self.gpin = pin
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.gpin, gpio.OUT)
        gpio.output(self.gpin, 0)
        # print("__magnet init__")

    def __del__(self):
        gpio.output(self.gpin, 0)
        # print "__deleted__"

    def up(self):
        gpio.output(self.gpin, 1)

    def down(self):
        gpio.output(self.gpin, 0)

if __name__ == "__main__":
    print("begin")
    pin_enb = 12
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin_enb, gpio.OUT)
    gpio.output(pin_enb, 1)
    time.sleep(2)
    gpio.output(pin_enb, 0)