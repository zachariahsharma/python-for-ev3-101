# Hello, World
 
## The Starter code
 
When you open a new project it looks something like this:
 
```python
#!/usr/bin/env pybricks-micropython                                             1
 
from pybricks import ev3brick as brick                                          2
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                               SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
# Write your program here                                                       3
brick.sound.beep()                                                              4
 
```
 
Okay let's look at the first line(1) it has a jumble of a lot of different stuff, so what is that? Well it's basically telling python to use micropython and not just regular python. Okay fine then what's all those other stuff(2) basically that is just a bunch of imports basically stuff written in other files telling the brick how to work. Don't get too flustered by it, that is only what is for the brick. Micropython in general isn't hard. Let's look at the next line(3), wait, why can you just write like everything is normal, just proper english? That is a comment, if you put a hashtag in front of what you want to type python will just ignore it. So all of that brings us down to the last line(4), the real micropython, it really is just a simple beep. Out of all of this I would say the thing we will use the most is the comment line. "Why?" you may ask, it's because when you make it easy for other people to go in and know exactly what's going on. Also if you make a mistake and there is a bug the computer may tell you the line where there is a mistake, but sometimes the error might be in a few lines before or in a whole different program. Once you make a mistake you can read the comments for that area  and make sure the line that it's commenting is actually doing what it's supposed to be doing.
 
Okay this is great but this isn't really what I am going to talk about in this chapter.
 
***
##The Hello World Code:
 
```python
#!/usr/bin/env pybricks-micropython
 
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                               InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                               SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
brick.display.clear()
 
brick.display.text("Hello World")
```
 
Okay so we know the top part, those are the imports, but what's the rest of it? Let's take it step by step.
 
```python
brick.display.clear()
```
 
This is clearing the display, it's pretty straightforward, I mean it literally says that on it. Micropython really isn't difficult, you just have to take your time to learn it. Okay big whoop we cleared the screen, now what. Okay now what we do is we display the words:
 
```python
brick.display.text("Hello World")
```
 
Hurray we finished it, this really wasn't that hard right? I think now we can move on to things that are a little more harder.
**Note: You have to put this code in your main file or else it won't run**
 
When we run this we see that it only flickers hello world in the top left corner. We will resolve this bug in later chapters.
 
[Click This to Go to the Second Chapter: Variables, Strings, Integers and Booleans](third_program.md)
 


