---

title: Symmetrical Snowflake
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "Draw a snowflake with a random pattern."

# exact sizes to match your project. PNG or JPG.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter.png
# Resides in /images/ folder
image:
  feature: 2016-02-17-snow-flake-feature.svg
  teaser:  2016-02-17-snow-flake-teaser.gif

video:
  teaser: 2016-02-17-snow-flake-teaser.mp4

# Add only if project is updated after publication. 2016-12-25
modified:

share: true
author: false
comments: yes
---

This program builds a random 3x3 image for the display. This then rotated 45&deg; 3 times fro each corner of the micro:bit.

{% highlight python %}
{% include_relative 2016-02-17-snow-flake.py %}
{% endhighlight %}
