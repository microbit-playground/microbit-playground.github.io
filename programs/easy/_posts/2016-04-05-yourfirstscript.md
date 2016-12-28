---

title: Your first script for the micro:bit
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "Say hi to an astronaut."

# exact sizes to match your project. PNG or JPG.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter.png
# Resides in /images/ folder
image:
  feature: 2016-04-05-your-first-script.svg
  teaser:  2016-04-05-your-first-script.png

# edit /data/author.yml with your details for info box. Please consider attributing your contribution to inspire kids.
# the author box contains links to twitter/websites etc

# Add only if project is updated after publication. 2016-12-25
modified:

share: true
author: false
comments: yes

---


## Your First MicroPython Script
--------------------------------

### Learning Objectives

After completing this tutorial, you will be able
 * to explain what a sequence is
 * to program a sequence of words or short phrases on the microbit.

### What You Need to Know First

Nothing at all. This is your first script!

If you know a little Python, skip to the next section.

If you have never used Python or you want some reminders, read on.
Python is a high level language: that just means that it uses words that are like the English language we humans use. But beware – spelling, capitals, order all matter.

The Python website says that when you download Python for your computer, it comes “with batteries”. That means that you can start using it immediately, not like those toys that need a set of batteries you haven’t got. But, as with a Lego set, you can get extra kits called modules. We will be using a special module for the microbit.
 
In the world outside school people use Python for many different purposes, including writing games, sifting through websites and data and, believe it or not, dentistry. Google uses Python and if it’s good enough for them, it’s probably good enough for us.
### Sequences

A sequence is just a series of statements or commands in order, one after the other.
Computers are very good at carrying out instructions but they need to be told the order. Computers control our traffic lights. Does order matter? Would you like the lights to go red for the traffic to stop first before they go green for you as a pedestrian? Does the order matter?

If you are making tea for yourself or your parents, does it matter whether you heat the water before you put it in the cup – or the teapot if you are being a little old skool?

### A Little Planning

Jot down on paper or on your computer two or three words making up a short phrase.
It’s a tradition that programmers start with “Hello World”. You could say “hello” to your school or your city or your favourite football club or – well, you choose.


Now jot down another short phrase.
You will program the microbit to display the first phrase, pause for a couple of seconds, then display the second phrase. That’s a sequence with three steps.
### Open the Editor
Double click the Mu icon on your desktop. The Editor will open.

![Mu Editor for MicroPython](images/chp2/Mu_editor.png)
 
The first line is an instruction to import all of the commands and functions from the module called microbit. Remember that a module is like a kit of extra parts: the microbit kit has commands and functions for using the LED matrix, the buttons and all the other components you don’t find on a desktop or laptop computer.
Line 3 is a comment just telling us that we can enter our code below. Comments begin with a hash (not a hashtag, this isn’t Twitter). Computers ignore comments, they are just for us. It’s obvious that we enter code, so go ahead and delete the comment.

### Now for the code

#### First Phrase

To display my first phrase I enter code:

```python
from microbit import *

display.scroll('Hi, Tim', 400)
```
 
400 is a measure of speed. More about this later.
My message might be visible in space but probably not. To see if it is visible in school, click on Flash. The orange LED on the back of the microbit will flash. When it has finished flashing, you will
 
* see your message scroll across the screen or

* get a message beginning  “Line 3” with details of an error.

If you saw an error message, look carefully at your script and correct any typos or missing quote marks. Try again.
 
#### A Short Pause

Enter this code on the next line:

```python
sleep(1000)
```
 
sleep is a function that makes the microbit’s controller chip wait – doing nothing – for the number of milliseconds in the brackets. Programmers call the number in brackets an argument. 
How long a pause will an argument of 1000 produce?

#### Second Message

Enter this code on the next line:

```python
display.scroll('from planet Earth', 400)
```
 
Choose Flash to send your code to the microbit.

Troubleshoot if you get an error message. There’s no need to ask your teacher for help – you and your partner can work this one out yourselves.

### Save

Choose Save and save your script in your work area with a name that has no spaces. Don’t forget the .py extension to show that you are saving a Python file.

### Tinker/ Experiment

The message seemed a bit slow to me. What do you think? Try changing the argument from 400. Up or down? Don’t ask, just try it.

Does the microbit sleep for too long or not long enough? Try changing the argument.

### Extension

Let’s say ‘Hi’ to students in your class or form.

We will say ‘Hi’ to them in a random order. We don’t want to be accused of having favourites!
We are going to need a list of students’ names.

We are also going to need to import a module with functions for making random selections.
Usually we import all the modules at the top of the script.

In the Mu editor, choose New.
If you see a blank screen, add these lines:

```python
from microbit import *
import random
```

 The first line imports all the functions from the microbit module.

The second line imports the random module but not its functions. When we want to use a function from the random module, we have to use the module’s name and the function’s name. You will see this in action shortly.

Next we need a list.

We will make a list and assign it to a variable “friends”. This means that “friends” is the name for the space in memory where we are saving our list of friends.

Lists are enclosed in square brackets. Each item – each friend – is separated by a comma.

```python


friends = ['Rob', 'Jenny', 'Fred', 'Nirmal', 'Lucia', 'Nazmin', 'Cris']
``` 

Now for the random choice:

```python




display.scroll(random.choice(friends), 200)
```
 
Choose Flash.

If you get an error, check your code very carefully. Have you got matching brackets? In line 6 you should have two opening brackets and two closing brackets.
The microbit should display the name of one of your friends. Then the matrix goes blank.
Press the reset button on the back of the microbit. Does it display the same name or a different name? Try it several times.

Save your script. Mine is called randomfriends.py (no spaces!)
 
### Tinker/ Play around

You could make a different list, perhaps a list of greetings.

Your code, your ideas!
