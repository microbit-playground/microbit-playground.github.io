---
layout: developers
title: "Why use the micro:bit to Teach Python?"
modified: null
excerpt: "The problems of using python in school are many. The micro:bit may help change all that!"
author: jez_dean
image:
  feature: "teachers-why-mu.svg"
shareable: "yes"
published: true
permalink: teachers/why-python-microbit
comments: true
---

For non-teachers, try to picture this scene: A class of 11 year-olds have come to your computer science lesson having spent the last hour running around in PE. You want to introduce Python programming. You need to make it interesting. Where do you start?

Honestly. It's hell! And it's not made any easier by Python. The problems below can all be solved by the micro:bit.

### 'Python is Boring' 

![Writing python into a console](/images/teachers-python-shell.png)

The entry point to Python is high. It's hard for beginners to write programs with the _wow factor_. Even giving kids a Python script to mash can be a challenge. As a result, Python can earn the reputation of being 'boring'. 

A kiss of death from kids.

### 'Python is Too Hard' 

Small Basic is an amazing language from Microsoft. It has an awesome IDE and the syntax is easy to understand. The `Turtle` object is easy to manipulate and no dependencies are visible to the user. 

![Comparison of Python and Small Basic](/images/teachers-python-small-basic.png)

Python's IDLE is amazing but it's too much for 11 year-olds graduating from Scratch. Many school networks refuse to install Python because of perceived security risks. As a result, it's run within a virtual machine so there's that palaver to deal with too.

### 'I can't run it home! What's Visual C++ 9?'

Kids make the most progress when they can program at home. This is easy with Scratch and Small Basic but not so with Python: 

1. Install Python 3.
2. MS Visual C++ so you can compile the dependencies of Turtle.
3. Right click Start button and click `Command Prompt (Run as Administrator)`
4. pip install turtle
5. pip install etc. 

---

# Python on the micro:bit

The _killer feature_ of the micro:bit is its ability to run Python. It lowers many of the barriers listed above:

### Simple Language

{% highlight python %}
from microbit import *
while True:
    if button_a.is_pressed():
        display.show(Image.ANGRY)
{% endhighlight %}

The micro:bit Python module makes coding really, really straightforward. Beginners can understand even advanced programs thanks to the simplicity of the microbit module.

The methods and classes are simple and make intuitive sense. The heavy-lifting is abstracted away from the programmer which results in clean, readable code.

### Use it at Home

mu is the simple IDE for Python on the micro:bit. The children just download it and double click it; it doesn't even need installing. In schools it can be run from a network share and there's no need for a virtual machine.

A Python editor can even be used from the browser by visiting microbit.co.uk.

### It makes Python Fun

Children can create _meaningful_ programs in a few lines of code. Write a compass. Make a pong game. Write a smiley animation. Code a magic 8 ball... 

... anything but moving a turtle around!







