#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase, Stop
from pybricks.parameters import Port
from pybricks.tools import wait
def run():
    motor_b = Motor(Port.B)
    motor_c = Motor(Port.C)
    motor_b.run_angle(500, 720, Stop.BRAKE, False)
    motor_c.run_angle(500, 720, Stop.BRAKE, True)
    motor_b.run_angle(-500, 720, Stop.BRAKE, False)
    motor_c.run_angle(-500, 720, Stop.BRAKE, True)