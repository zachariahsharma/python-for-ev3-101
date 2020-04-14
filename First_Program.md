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

Okay lets look at the first line(1) it has a jumble of a lot of different stuff, so what is that? Well it's basically telling python to use micropyton and not just regulat python. Okay fine so then whats all those other stuff(2) basically that is just a bunch of imports basically stuff written in other files telling the brick how to work. Don't get to flustered by it, that is only what is for the brick. Micropython in general isn't hard. Lets look at the next line(3), wait, why can you just write like everything is normal just proper english? That is a comment, if you put a hashtag in front of what you want to type python will just ignore it. So all of that brings us down to the last line(4), the real micropython, it really is just a simple beep. Out of all of this I would say the thing we will use the most is the comment line. "Why?" you may ask, its becuase when you make it easy for other people to go in and know exactly whats going on. Also if you make a mistake and there is a bug the computer may tell you the line where there is a mistake, but sometimes the error might be in a few lines before or in a whole different program. Once you make a mistake you can read the comments for that area  and make sure the line that it's commenting is actually doing what its supposed to be doing.

Okay this is great but this isn't really what I am going to talk about in this chapter.

***
**The Hello World Code:**

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

brick.display.text("Hello", (60, 50))

brick.display.text("World")
```

Okay so we know the top part, those are the imports, but whats the rest of is? Lets take it step by step.

```python
brick.display.clear()
```
This is clearing the display, its pretty straightforward, I mean it literally says that on it. Micropython really isn't difficult
