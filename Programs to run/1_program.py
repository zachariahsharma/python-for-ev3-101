#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor) 
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_b.run_angle(500, 720, Stop.BRAKE, False)
motor_c.run_angle(500, 720, Stop.BRAKE, True)
motor_b.run_angle(-500, 720, Stop.BRAKE, False)
motor_c.run_angle(-500, 720, Stop.BRAKE, True)