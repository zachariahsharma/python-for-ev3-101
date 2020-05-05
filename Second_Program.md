# The Dog Goes,"Bark"

## The Sound Block

In this chapter we'll talk about sound block. But before we talk about that we need to understand the importance of sound blocks. They are important because when you program, there will be times when you make a mistake and you can't figure out where it is. To solve this problem you can put a sound block in different places of your program so that when you run it you know where the problem is, this is called "Troubleshooting." Now lets create a new project called ***The dog goes,"Bark."*** This project will be about how to use sound on the EV3. Once you have created your project input this in.
```python
#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.sound.file(SoundFile.DOG_BARK_1)
```
This is a sound block. The *"brick.sound.file"* is pretty easy to understand, its telling python that whatever you put in the parentheses will be a sound file. The sound file starts with very suprisingly *"SoundFile"* You might be wondering *Why did they put that SoundFile in front of the name of the sound file? Are they just trying to waste our time with it?* Well actually its to make it easier for them, basically when they create all the stuff for the brick, it is really complex for them to just put the name of the sound file. This is because they might then encounter many files that have the exact same name. To counter this they put that *"SoundFile"*. We will use sound files a lot in later chapters. 

## Errors

You might be wondering what some of the errors are, they are very imporant to know becuase it is inevitable that you will come across them. Although personally I really like to avoid errors, sometimes you want to get a error so you know you got something right. That might sound absoulotly rediculous, I mean really, the point of the errors are to tell you you're wrong. Well yeah, but also you might be just testing if something gives a error, though we'll talk more on this concept later. When you come across a error you will find that there are many different errors that you will come across, but I will show you the most common ones:
- Type Errors
- Syntax error

Lets start with the first one. Type Errors occur when something is identifieed as something else but they are 2 things that can't be identified together. Okay that probably didn't make any sense. Basically it means that if I said that I want you to tell me a number 1-10 but you told me "Hi", what would happen then? Well, I would tell you that you are wrong and a computer would give you a type error.


The second type of error is the syntax error, this error happens when the computer is just confused. An example of this would be when you make a sound program, and it looks something like this
```python
#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.sound.file(SoundFile.DOG_BARK_1)

This line would give you a syntax error because I am openly typing and python has no idea what to make of it.
```

This is what happens when you run it:
```
Starting: brickrun --directory="/home/robot/python-for-ev3-101" "/home/robot/python-for-ev3-101/main.py"
----------
Traceback (most recent call last):
  File "/home/robot/python-for-ev3-101/main.py", line 21
SyntaxError: invalid syntax
----------
Exited with error code 1.
```

Wow! Thats a lot its saying. Basically the first line is showing that the brick started running it, the 3rd line is saying that that is the most resent call, The 4th line is where it is, and the fifth line is saying what the error is. It says its a syntax error but it doesn't tell you wht is wrong other than 