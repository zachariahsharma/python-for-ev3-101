# The Dog Goes,"Bark"
 
## The Sound Block
 
In this chapter we'll talk about sound block. But before we talk about that we need to understand the importance of sound blocks. They are important because when you program, there will be times when you make a mistake and you can't figure out where it is. To solve this problem you can put a sound block in various places of your program so that when you run it you know where the problem is. This is called "Troubleshooting." Now lets create a new project called ***The dog goes,"Bark."*** This project will be about how to use sound on the EV3. Once you have created your project input this in.
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
This is a sound block. The *"brick.sound.file"* is pretty easy to understand, it's telling python that whatever you put in the parentheses will be a sound file. The sound file starts with very surprisingly *"SoundFile"* You might be wondering *Why did they put that SoundFile in front of the name of the sound file? Are they just trying to waste our time with it?* Well actually it's to make it easier for them, basically when they create all the stuff for the brick, it is really complex for them to just put the name of the sound file. This is because they might then encounter many files that have the exact same name. To counter this they put that *"SoundFile"*. We will use sound files a lot in later chapters.
 
## Errors
 
You might be wondering what some of the errors are, they are very important to know because it is inevitable that you will come across them. Although personally I really like to avoid errors, sometimes you want to get an error so you know you got something right. That might sound absolutely ridiculous, I mean really, the point of the errors are to tell you you're wrong. Well yeah, but also you might be just testing if something gives a error, pretend you're telling your robot to turn left 2 degrees but when you do that you can't tell whether you moved at all because it's such a small movement, to solve this you could move 100 degrees which will be wrong but you can check whether you moved right or left. When you come across a error you will find that there are many different errors that you will come across, but I will show you the most common ones:
- Type Errors
- Syntax error
 
Let's start with the first one. Type Errors occur when something is identified as something else but they are 2 things that can't be identified together. If that didn't make sense, it means basically that if I said "I want you to tell me a number 1-10," but you told me "Hi", what would happen then? Well, I would tell you that you are wrong and a computer would give you a type error. This is an example of what you would do to get a type error.
 
```python
 
#!/usr/bin/env pybricks-micropython
 
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                               SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
variable = float("hi")
```
The *float* This is telling Python that whatever is within the parentheses is going to be a float or a decimal but "hi" is most definitely a string and will not be changed into a float.
 
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
 
Wow! That's a lot to say. Basically the first line is showing that the brick started running it, the 3rd line is saying that that is the most recent call, The 4th line is where it is, and the fifth line is saying what the error is. It says it's a syntax error but it doesn't tell you what is wrong other than that it has the wrong syntax.


