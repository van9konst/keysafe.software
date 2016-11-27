from motor_driver_a4988 import MotorDRV_a4988
from magnet_driver import Magnet
from constants import *
from time import sleep

if __name__ == '__main__':
    mtr1 = MotorDRV_a4988(motor1_step, motor1_dir, motors_enable)
    mtr2 = MotorDRV_a4988(motor2_step, motor2_dir, motors_enable)
    mgn = Magnet(magnet)

    pppath = "50011 50012"
    for comnd in pppath.split():
        motor = int(comnd[-1])
        direction = int(comnd[-2])
        steps = int(comnd[:-2])
        print comnd
        if motor is 1:
            mtr1.spin(steps, direction)  # 500 1 1
        if motor is 2:
            mtr2.spin(steps, direction)

    for comnd in pppath.split()[::-1]:
        print comnd
        motor = int(comnd[-1])
        direction = 0 if int(comnd[-2]) == 1 else 1
        steps = int(comnd[:-2])
        if motor is 1:
            mtr1.spin(steps, direction)  # 500 1 1
        if motor is 2:
            mtr2.spin(steps, direction)

            # mgn.up()    # 13
            # mtr1.spin(500,1)# 500 1 1
            # mtr2.spin(500,1)# 500 1 2
            # sleep(1)
            #
            # mtr2.spin(500,0)
            # mtr1.spin(500,0)
            # mgn.down() # 03
