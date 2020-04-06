#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase, Stop
from pybricks.parameters import Port
from pybricks.tools import wait
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
# okay everything above should make sense now if it doesn't go to the first program and everything will be explained there
# what we are going to do now is make the ev3 robot move forward turn around and move back to where it was
# lets start with moving forward, we already know how to do that, so let's do it
motor_b.run_angle(500,720,Stop.BREAK,False)
motor_c.run_angle(500,720,Stop.BREAK,True)
# For this task I also have to introduce a new sensor: the Gyro sensor!
# the point of this sensor is to look at what angle you have turned so this will be important to use
# okay so now lets think about the logic
# the logic is that we have to have the robot turn until the gyro has sensed that we have turned 180 degrees
#lets initialize the gyro now
Gyro = GyroSensor(Port.S1)# This is saying that at port 1 (which is a sensor port on a ev3that's why it has a "S") there is a gyro sensor
# okay now we have initilized it now what? Now we have to make the robot constantly check so we will use a while loop, it looks like this
#while True:
#   pass
# so we start by saying while true which means just constantly changing but that's not neccarily what we want, we want it to check to see what the gyro value is
while gyro.angle() <= 180: # so now we have said that while the gyro value is less than or equal to 180 then we will run everthing else. Why less than or equal why not less than? Well it's because we need to make sure that there is a possibility that it might be 18 degrees
    motor_b.run_angle(100,10,Stop.COAST,False)# this is saying to turn one motor, motor_b 10 degrees at speed 100. You want the speed to be small and you want the amount of degrees small as well, we want the speed to be small because we want it to slowly reach your target angle so it's accurate, we want the distance to be small so that we can movemore precisly but not to jerky. Though if these don't fit your robot well you can change them at any time
# Harray! we have now turned so now the task at hand is that we need to make it move make to where we started so what we are going to do is drive back to the place we went originally
#so lets do that:
motor_b.run_angle(500,720,Stop.BREAK,False)
motor_c.run_angle(500,720,Stop.BREAK,True)
#this will work unless your robot has your large motors on the opposite side as mine if your robot starts spinning in circles switch the ports of your large motors
#Harray we did it! Wait that's peculiar it was a
