__author__ = 'name'
import RPi.GPIO as GPIO
import time
#git pass = "8Quelarfyi41"

def show_foo_name(fn):
    def something():
        print "line:  " + fn.__name__

    return something


class MotorDRV(object):
    seq = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1],
           ]
    ctrl_pin = None

    # @show_foo_name
    def __init__(self, ctrl_pin=[3, 5, 7, 8]):
        self.ctrl_pin = ctrl_pin
        GPIO.setmode(GPIO.BOARD)
        for pin in ctrl_pin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        print("__initiated__")

    def spin(self, step_count, ctrl_pin, sleep_time):
        try:
            for i in range(step_count):
                for step in range(4):
                    for pin in range(4):
                        GPIO.output(ctrl_pin[pin], self.seq[step][pin])
                    time.sleep(sleep_time)
        except KeyboardInterrupt:
            self.clear_ports()
            print("EXIT!")

    def spin_left(self, step_count=100, sleep_time=0.005):
        self.spin(step_count, self.ctrl_pin, sleep_time)

    def spin_right(self, step_count=100, sleep_time=0.005):
        self.spin(step_count, self.ctrl_pin[::-1], sleep_time)

    def clear_ports(self):
        for pin in range(4):
            GPIO.output(self.ctrl_pin[pin], 0)

    def __del__(self):
        self.clear_ports()
        GPIO.cleanup()
        print "__deleted__"


if __name__ == "__main__":
    mtr1 = MotorDRV()
    mtr1.spin_right(50, 0.01)
    mtr1.spin_left(50, 0.01)

