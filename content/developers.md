---
layout: developers
title: How to Contribute
modified: null
excerpt: "Write your Python program and then send it to micro:bit playground for inclusion."
author: jez_dean
image: 
  feature: "developers-send-python-code-feature.png"
shareable: "yes"
published: true
permalink: developers/
---


This website collects examples of muPython code kids can hack and mash. If you have written Python code for the Micro:bit please, please send it here. 

Here's how to do it in a sentence: clone the repo and send it back with micro:bit code and documentation.

## Contributing in 6 Steps

1. Clone the [repo][3]
2. Document your code with `/template/program-template.md` or `/template/program-template-bare.md`.
3. Copy your `.py` and `.md` files to `/programs/easy/_posts/` or `../medium/...` or `.../ninja/...` depending on dificulty. Naming scheme is `2016-02-24-my-program.*`.
4. Edit `/template/program-template-header.svg`, add your program name with a text editor and save to `/images/`.
5. Copy any images to `/images/` with the same file name as your project, eg. `2016-02-24-my-project-1.jpg` and `2016-02-24-my-project-2.png`
6. Pull request

I'll write up any documentation if you're unsure or you just want to push Python code.

## Don't use GitHub?

Send the code you've written to jez@geekteacher.co.uk. Include a brief write up and some photos. I'll add it to the website.

## Running this Website

You may wish to preview what your contribution looks like before submitting. To do this you'll need to run Jekyll. **It couldn't be easier**.

1. `git clone etc...`
2. `cd /mu-project/` change into this project's directory.
3. `bundle install`
4. `bundle exec jekyl`
5. Visit `localhost:4000` in your browser.

## Running this Website on Windows

It's easy to run this website under Windows.

* Download and extract this website into a directory.
* Download and install [Ruby 2.2.4][1].

You must also install the Ruby Dev Kit to build some Ruby gems. There are instuctions and the download [on this website][2].

* Double click `run.bat` in the directory you made in step 1.
* Visit `localhost:4000` in your browser.

And yes. It is that simple! Email your `.py`, `.md` and images. I'll add them to the site.

## Templates

You can pick from two templates in the  `/templates` directory.

| Template Name | Description | HTML View | Raw Markdown |
|---------------|-------------|-----------|--------------|
| `program-template.md` | Full template with all the features available to document your code | [View](../templates/program-template.html) | [View](https://raw.githubusercontent.com/microbit-playground/microbit-playground.github.io/master/templates/program-template.md) |
| `template_program-bare.md` | Empty template for minimal write up (but please send images!) | [View](program-template-bare.html) | [View](https://raw.githubusercontent.com/microbit-playground/microbit-playground.github.io/master/templates/program-template-bare.md) |

I recommend using `template_project.md` as it has examples of all the features.

[1]: http://rubyinstaller.org/downloads/
[2]: https://github.com/oneclick/rubyinstaller/wiki/Development-Kit
[3]: https://github.com/microbit-playground/microbit-playground.github.io