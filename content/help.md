---
layout: page
title: "Getting Started"
date: 2015-06-25T13:57:25-04:00
modified: 2016-01-19
excerpt:
tags: [test1, test2]
image:
  feature: getting-started-featured.jpg
  teaser: 850x400.png
  thumb: 120x120.gif
share: false
permalink: getting-started/
---


{% include toc.html %}

#### Where do I download Mu?

Mu is the editor used to write python code for the micro:bit. It's an [open source project](https://github.com/ntoll/mu) written by software developers to encourage kids (& adults!) to write code.
To download it:

1. Go to [the mu download page](http://codewith.mu/)
2. Click your operating system.
3. Scroll to the bottom of the page and click the final file.
4. Download and install.

#### What if I can't install Mu?

Visit the official BBC <a href="http://microbit.co.uk/">microbit.co.uk</a> website, click on "Create Code" and select Python. Beginner friendly help for this editor can be <a href="https://microbit.pythonanywhere.com/help.html">found here</a>.

#### But I use a Chromebook!

We have you covered! There is a simple MicroPython editor for the micro:bit alreay in the <a href="https://chrome.google.com/webstore/detail/micropython/lhdjeebhcalhgnbigbngiaglmladclbo">Chrome store</a>. :-)

#### Where can I get help?

* [Micro:bit Tutorials](https://microbit-micropython.readthedocs.org/en/latest/tutorials/introduction.html) - Beginner friendly tutorials for MicroPython on the BBC micro:bit.
* [mu Editor](https://github.com/ntoll/mu) - A code editor for Python on the micro:bit.
* [Micro:bit MicroPython API](http://microbit-micropython.readthedocs.org/en/latest/microbit_micropython_api.html) - Developer-friendly API docs for MicroPython.

## What is...

#### What's MicroPython?

[MicroPython](https://micropython.org/) is a variant of Python that runs on microcontrollers like the micro:bit. Some of the standard features of Python have been removed so it can fit on a microcontroller.

#### What's Mu?

[mu editor](https://codewith.mu/) is a text editor you can use to write Python code. _mu_ is free and open source. It is written by software developers because they want to help you learn code.

## Common Problems

#### Windows Cannot Connect to the Micro:bit

If you're on Windows you may require a driver to fix your problem.

You can download it from ARM who designed some of the chips inside the micro:bit.

[Driver Download](https://developer.mbed.org/handbook/Windows-serial-configuration)

#### Linux Cannot Connect to the MicroPython REPL

You may need to add yourself to the `dialout` group so Linux can make a USB/serial connection to the device in order to connect to the Python REPL. You'll need to run a command like this: `useradd -G dialout YourUsername`
