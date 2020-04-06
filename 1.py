#!/usr/bin/env pybricks-micropython
# Author: Zachariah Krish Sharma
# Version: 0.1

# the funky thing up top is to tell python that we are using micropython not regular python
# okay but what's that hash tag beside these things? that is the comments it tells python to forget whatever is after it
# These are imports they are used to inform python how to use the brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase, Stop
from pybricks.parameters import Port
from pybricks.tools import wait

# This is for initializing the large motors on your ev3 although this could also be used for medium motors
# It tells python that We are going to use motors and their names are motor_b and motor_c
motor_b = Motor(Port.B)#We are setting motor_b to the known function that micropython has pre downloaded "Motor" and it has a parameter that needs the port in our case it's prot B on the ev3
motor_c = Motor(Port.C)# We are setting motor_c to the function "Motor" at port C

# My first program is just moving forward and backards which in micropython is simple, but the thing is that it isn't one line with micropython you have to control them seperatly
motor_b.run_angle(500, 720, Stop.BRAKE, False)# this is telling micropython that your using motor_b to move froward at a speed of 500 and moving 720 degrees which is 2 rotations
# the third parameter is telling micropython that you want to break at the end, if you want to coast change the "BREAK" to "COAST" 
# and the last parameter is telling micropython that you have to go to the next line as well becuase we are also running the next motor
motor_c.run_angle(500, 720, Stop.BRAKE, True)# this is telling micropython to now move motor_c
# since the last parameter says true then that means we aren't doing anything else at the same time
# okay now we have made the robot move forward, okay now how do we move backwards?
# in our previous one we moved at a speed of 500 and a distance of 720 to move backwards wwe have to make one of those negative I usually make the speed negative becuase thats how I was taught and what ev3 normally does
#So it will look something like this
motor_b.run_angle(-500, 720, Stop.BRAKE, False)# in this line we have done literally exactly the same thing as the previous one accept we have made the speed negative, that's all you have to change to make it backwards
motor_c.run_angle(-500, 720, Stop.BRAKE, True)# this is also exactly the same accept I have negated the speed
#and there you go, that's how you make your ev3 move forwards and backwards using micropython
#if you have a robot that has upside down motors your speed moving forward will be negative and your speed moving backwards will be positive
