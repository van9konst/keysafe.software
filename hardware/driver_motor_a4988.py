# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time


class MotorDRV_a4988(object):
    def __init__(self, steps=3, direct=5, NOTenb=11):
        """
        :param steps: pin generate controll signal CS*
        :param direct: pin define roll dirrection
        :param NOTenb: pin define driver enable/disable.
        gpio.output(NOTenb, 0)==enable # if NOTenb set to 1 -> driver off
        """
        self.direction = steps
        self.step_crc = direct
        self.NOTenb = NOTenb
        gpio.setmode(gpio.BOARD)
        for pin in ctrl_pin:
            gpio.setup(pin, gpio.OUT)
            gpio.output(pin, 0)

    def spin(self, steps):
        gpio.output(self.NOTenb, 0)  # On driver

        # parametrs for acceleration motor work t==time
        c_steps_accelerate = 100  # steps count for acceleration
        t_step_max = 0.001
        t_step_start = 0.004
        t_step_cur = 0
        t_step_value = (t_step_start - t_step_max) / c_steps_accelerate
        t_step = t_step_start

        for i in range(0, steps):
            cs ^= 1
            gpio.output(self.step_crc, cs)

            # cheking for reaching END bounds position #last 100steps
            if (i > steps - c_steps_accelerate) and (t_step < t_step_start):
                t_step += t_step_value
                time.sleep(t_step)
            # cheking if we still in BEGIN bounds position #first 100steps
            elif (i < c_steps_accelerate) and (t_step > t_step_max):
                t_step -= t_step_value
                time.sleep(t_step)
            # bounds between  begin_end # [x+100..x-100]
            else:
                time.sleep(t_step_max)
        gpio.output(self.NOTenb, 1)  # Off driver


if __name__ == "__main__":
    print("begin")
    pin_dir = 3
    pin_step = 5
    # pin_dir = 7
    # pin_step = 8
    pin_enb = 11
    gpio.setmode(gpio.BOARD)
    # gpio.setup(7, gpio.OUT)
    # gpio.setup(8, gpio.OUT)
    # gpio.setup(7, gpio.OUT)
    # gpio.setup(8, gpio.OUT)
    gpio.setup(pin_dir, gpio.OUT)
    gpio.setup(pin_step, gpio.OUT)
    gpio.setup(pin_enb, gpio.OUT)
    # gpio.output(pin_enb, 1)
    # time.sleep(10)
    # gpio.output(pin_enb, 0)
    t_step_max = 0.001
    t_step_start = 0.004
    t_step_cur = 0
    steps = 900
    c_steps_accelerate = 100
    t_step_value = (t_step_start - t_step_max) / c_steps_accelerate
    t_step = t_step_start
    gpio.output(pin_enb, 0)
    for j in range(1, 5):
        gpio.output(pin_dir, j % 2)
        cs = 0  # control signal
        for i in range(0, steps):
            cs ^= 1
            gpio.output(pin_step, cs)
            if (i > steps - c_steps_accelerate) and (t_step < t_step_start):
                t_step += t_step_value
                time.sleep(t_step)
            elif (i < c_steps_accelerate) and (t_step > t_step_max):
                t_step -= t_step_value
                time.sleep(t_step)
            else:
                time.sleep(t_step_max)

        time.sleep(0.5)
    gpio.output(pin_enb, 1)
    # gpio.cleanup()
