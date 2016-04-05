---
layout: page
title: "Help"
date: 2015-06-25T13:57:25-04:00
modified: 2016-01-19
excerpt:
tags: [test1, test2]
image:
  feature: getting-started-featured.jpg
  teaser: 850x400.png
  thumb: 120x120.gif
share: false
permalink: help/
---

{% include toc.html %}

## Editor Options

There are two options: you can write code in the online editor or download an editor to work on your desktop.

### Online Editors

[microbit.co.uk](https://www.microbit.co.uk/create-code) has four different editors. In order of difficulty, these are:

* Microsoft Block Editor: Block-based editor with 'virtual' micro:bit to test code on.

* Code Kingdoms: Block-based editor with hints of javascript.  Also has a 'virtual'

* Touch Develop: VB-inspired code with friendly introduction to the micro:bit's functions.

* Python: Purely text-based programming. It's easier than it looks!

### Offline Editor

Only Python offers an offline editor called mu. It's simple to use and can be downloaded from the [mu website.](https://github.com/ntoll/mu)

Mu is open source and written by software developers to encourage kids (& adults) to write code. It's available for Windows, OSX, Linux (Raspberry Pi) and even the [Chromebook!](https://chrome.google.com/webstore/detail/micropython/lhdjeebhcalhgnbigbngiaglmladclbo). 

## Common Problems

#### Windows Cannot Connect to the Micro:bit

You may require a driver to communicate with the micro:bit. 

You can download it from ARM who designed some of the chips inside the micro:bit.

[Driver Download](https://developer.mbed.org/handbook/Windows-serial-configuration)

#### Linux Cannot Connect to the MicroPython REPL in mu

You may need to add yourself to the `dialout` group so Linux can make a USB/serial connection to the device in order to connect to the Python REPL. You'll need to run a command like this: `useradd -G dialout YourUsername`

## Frequently Asked Questions

### Is Python on the microbit complicated?

![image](/images/teachers-python-blocks.png)

No
