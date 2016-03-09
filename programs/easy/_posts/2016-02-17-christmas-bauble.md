---

title: Scrolling Bauble
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "Two lines of code to make a bauble."

# exact sizes to match your project. PNG or JPG.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter.png
# Resides in /images/ folder
image:
  feature: 2016-02-17-christmas-bauble-feature.svg
  teaser:  2016-02-17-christmas-bauble-teaser.gif

video:
  teaser: 2016-02-17-christmas-bauble-teaser.mp4

# Add only if project is updated after publication. 2016-12-25
modified:

share: true
author: jez_dean
comments: yes
---



<figure class="pull-right">
  <img src="{{ site.baseurl }}/images/2016-02-17-christmas-bauble-teaser.gif" alt="Right">
  <figcaption>Video by <a href="https://github.com/geekfish">geekfish</a>.</figcaption>
</figure>


This simple program displays "ho! ho! ho!" on the micro:bit. Let's go through it line by line... there are only two lines!

{% highlight python %}
{% include_relative 2016-02-17-christmas-bauble.py %}
{% endhighlight %}


### How it Works

#### Import the microbit module

`from microbit import *`

This imports the microbit module into the program. `*` imports _everything_ in the module. Start all your programs with this. It's simply telling Python that it'll need to use code to talk to the micro:bit.

#### Scroll the Text
`display.scroll("ho ho ho")`

Scrolls the text across the micro:bit's display. Everything inside the `"` is shown in the display. Characters within `"` are called strings.

### Reading the API

[The microbit API for the display module](http://microbit-micropython.readthedocs.org/en/latest/display.html) describes a `delay` parameter for the `scroll` method.

`display.scroll("ho ho ho", delay=500)` updates the display every 500 milliseconds (or half a second). It slows down the speed of the scrolling text.

The API documentation has information about every function and method. Try reading it when you're coding for ideas. It's not as scary as it looks! The Python community are also famously helpful - search online for mailing lists and message boards that may contain the help you need. If in doubt, ask for help with as much information as possible.

### Going Further

This only scrolls the message once. Can you make it repeat?
