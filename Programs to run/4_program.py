#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase, Stop
from pybricks.parameters import Port
from pybricks.tools import wait
def Gyro_Turn(Gyro,motor_b,motor_c,degrees,speed,clockwise):
    if clockwise:
        while Gyro.angle() <= degrees:
            motor_b.run(-speed)
            motor_c.run(speed)
    elif clockwise == False:
        while Gyro.angle() >= degrees:
            motor_b.run(speed)
            motor_c.run(-speed)
    motor_b.stop(Stop.BRAKE)
    motor_c.stop(Stop.BRAKE)
