#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase, Stop
from pybricks.parameters import Port
from pybricks.tools import wait
motor_b = Motor(Port.B)
motor_C = Motor(Port.C)
#Everything above should make sense if not refer to the first program
# What we are going to now is 