#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase, Stop
from pybricks.parameters import Port
from pybricks.tools import wait
def run():
    motor_b = Motor(Port.B)
    motor_c = Motor(Port.C)
    Gyro = GyroSensor(Port.S1)
    while Gyro.angle() <= 65:
        motor_c.run(900)
        motor_b.run(-900)
    motor_c.stop(Stop.BRAKE)
    motor_b.stop(Stop.BRAKE)