---
title: Microbit Counter
layout: project
excerpt: "Program to count how many times microbit's button was pressed."
image:
  feature: 2016-03-10-microbit-counter-feature.svg
  teaser: 2016-03-10-microbit-counter-teaser.gif
modified: null
share: true
author: false
comments: true
---

A simple program to count how many times the micro:bit's buttons have been pressed.

{% highlight python %} {% include_relative 2016-03-10-microbit-counter.py %} {% endhighlight %}

### How Has it Been Used?

![Photo: Jenny Thomas]({{ site.baseurl }}/images/2016-03-10-microbit-counter-1.jpg)

This  picture shows a scientist using the micro:bit to count krill. Krill are small organisms living in the ocean and scientists are interested in how pollution and climate change affects their population. The picture was taken onboard a ship in the South Atlantic!

There are many times you may need a counter; it's not just for counting krill!

### How it Works

#### `while True:`

This line puts the micro:bit into an endless loop. The program repeats everything that is indented.

#### `display.scroll`

The `display` module uses the `scroll` function to display the number of times `button_a` has been pressed. Only strings can be used with the `display` module.

#### `button_a.get_presses()`

`.get_presses` returns the number of times `button_a` has been pressed. This number is an integer.

#### `str(button_a.get_presses())`

`str(_stuff_)` converts everything inside `(` `)` to a string.

In this program it converts the number of times the button was pressed to a string. It still looks the same but python treats the numbers differently.


#### `display.scroll(str(button_a.get_presses()))`

__Python scrolls the number of button presses on the display.__ Easy! In Python the inner most command is executed first. In this program button_a.get_presses is executed first. Look at the flow of this line of code:

1. **button_a.get_presses()** : get the number of times `button_a` has been pressed
2. **str()** : convert the number of presses from an integer to a string
3. **display.scroll()** : scroll the converted number of presses

### Explainers

#### Strings & Integers

##### Strings

A string is a list of characters which python does not understand. Strings are always surronded by `"`quotation`"` marks.

```
"dog" + "cat"` = dogcat
```

We can also have numerals in a string:

```
"5" + "2"` = 52. 
```

Python does not understand a string. It only understands what the characters look like.

##### Integers

Integers are numbers. Python understands numbers and can perform calculations with them:

```
3 + 1 = 4 

1 * 4 = 16
```

Integers do not have `"`quotation'"` marks and they are treated by python as numbers--or integers!

Clear?

Earlier this year, micro:bits were sent to people all over the world. You can read about their advertures on [micro:bit world tour!](http://microworldtour.github.io/). There's also more about krill counting [on the website too.](http://microworldtour.github.io/microbit/macaroni.html)