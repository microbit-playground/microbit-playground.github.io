---
title: Spin the Bottle
layout: project
excerpt: "Spin the bottle and the micro:bit decides: truth or dare?"
image:
  feature: 2016-03-10-spin-the-bottle-feature.svg
  teaser: 2016-03-10-spin-the-bottle-teaser.gif
video:
  teaser: 2016-03-10-spin-the-bottle-teaser.mp4
modified: null
share: true
comments: true
author: false
---

Attach your micro:bit to a bottle and give it a spin. Will it be a truth or dare?

{% highlight python %} {% include_relative 2016-03-10-spin-the-bottle.py %} {% endhighlight %}

### How it Works

#### messages List

The program sets the value of `messages` to be a list of values. Each message ("Truth" and "Dare") is held in a list. `truth` and `dare` are both strings because they are surrounded by `"` quotation marks. 

Python knows it is a list because it is enclosed in square brackets and each item is separated by a comma. Lists can also be arranged on a single line:

{% highlight python %}

messages = ["Truth", "Dare",]

{% endhighlight %}

#### `while True:`

This creates a forever loop. Everything indented below this statement is repeated until the micro:bit is reset.

#### `if accelerometer.was_gesture("shake"):`

This `if statement` waits until the micro:bit is shaken. When it detects a shake, the micro:bit runs the code inside the `if` statement. The first command it executes clears the display. It then pauses for 1000 milliseconds.

#### `display.scroll(random.choice(message))`

To use `random.` it must be imported at the beginning of the program:

{% highlight python %}
from microbit import *
import random
{% endhighlight %}

A module (like `random`) is simply a library of pre-existing code for you to
re-use.

`random.choice(messages)` picks a random item in the `messages` list. It will pick either "Truth" or "Dare".

When the program picks a random choice it uses `display.scroll` to show message.

The loop then starts again and the micro:bit waits for a shake.

**RULE**: you only need to `import` a module if your code needs random numbers, makes a sound or uses a neopixel. Most of the time you will
just use `from microbit import *`
{: .notice-info}

### Making the Bottle

![Photo: Jo Claessens]({{ site.baseurl }}/images/2016-03-10-spin-the-bottle-1.jpg)

Be sure to put some stones inside so the micro:bit gets a good shake!
