---

# No longer maintained


Please don't make any changes! 

---

* micro:bit Playground website is at https://microbit-playground.co.uk
* All micro:bit programs can be [downloaded as a zip file](https://microbit-playground.co.uk/build/microbit-playground-code.zip).
* the project for the mu microbit python editor is [here on github.](https://github.com/ntoll/mu)

## About

micro:bit Playground publishes python code for kids to hack and mash (and hopefully learn something about python!)

This repo contains the code used to generate the website. It uses Jekyll---a ruby program---to turn markdown into beautiful pages.

## Contributing

Please (please! please!) send me your python code and a brief overview of how your program works. My email is jez@geekteacher.co.uk.

##### Easy Way:

1. Document your code with `/templates/program-template.md` [[download link]](https://raw.githubusercontent.com/microbit-playground/microbit-playground.github.io/master/templates/program-template.md)
2. Take photographs of your code or project.
3. Email them to me at jez@geekteacher.co.uk.
4. _Optional:_ Send through your name, photograph, website/twitter and a brief bio. These will be used to make you very cool author bio box!

##### Geeky Way:

1. `git clone git@github.com:microbit-playground/microbit-playground.github.io.git`
2. Document your code with `/templates/program-template.md` or `/templates/program-template-bare.md`.
3. Copy your `.py` and `.md` files to `/code/easy/_posts/` or `../medium/...` or `.../ninja/...` depending on difficulty. Naming scheme is `2016-02-24-my-program.*`.
4. Edit `/templates/code-template-header.svg`, add your project name with a text editor and save to `/images/`. It's just an `xml` file.
5. Copy any images to `/images/` with the same file name as your program, eg. `2016-02-24-my-code-1.jpg` and `2016-02-24-my-code-2.png`
6. Edit `authors.yml` in the `_data` directory with your personal information.
6. Pull request

## Running the Website on Localhost

##### Running & Install Jekyll

1. clone this repo
2. install bundler: `gem install bundler`
3. install required gems: `bundler install`
4. serve the website locally with installed gems: `bundle exec jekyll serve`
5. visit `http://localhost:4000`

The website loads the font Andika with inlined CSS from a CDN. This helps the page load quickly (300 - 600ms!) but means the website looks... _retro_ without an internet connection.

Although Andika is a big font to load--it's over 20k--it is beautiful. Do read more about [this typeface here.](http://software.sil.org/andika/)

##### Running `gulp`

_There's no need to run `gulp`_ it's very messy!

The website uses `gulp` to complete tasks for production. `gulp` requires `node.js` to be installed.

* in main directory run `npm install`
 * `gulp scripts` to minify & combine javascript
 * `gulp zip` creates a zip file of all the programs.
 * `gulp svg2png`to convert svgs to pngs. This is used to make PNGs for opengraph (pretty Twitter cards).

`gulp images` smushes images but do not use until a build/source directory for images is implemented.

##### Production / Development Environment

* `\_config.yml` loads variables for the production environment (eg. `url: https://github...`)
* `\_plugins\set_development_environment.rb` loads variables for development environment (eg. `url: http://localhost`)

Running the website on localhost loads the development variables from a plugin.
Running the website on Github use `_config.yml` production values since plugins are not used on github.

## TODO

* More programs
* Use gulp to build images from src/
* ~~build pretty header images for opengraph (twitter cards/facebook etc)~~
* Fix jshint error messages when running `gulp scripts`
* Remove numerals from zip download of python script.
* Add txt explainer about the programs
* Style guide & fix typos
  * micro:bit / Microbit / microbit
  * python / Python
  * licence / license
  * practice / practise
  * noun / verb
  * etc

## Elsewhere

There are other collections of code on the internet. Here's an incomplete list of awesomeness:

* [mavhc's gists][1] - A collection of ninja python programs
* [Whaleygeek's github][2] - A collection of games -- microbit Connect 4!
* [cpina's github][3] - Games & apps

[1]: https://gist.github.com/mavhc
[2]: https://github.com/whaleygeek/microbit_python
[3]: https://github.com/cpina/macaroni

## Contributing

Guidance on how to contribute is above or on the [developers page](https://microbit-playground.co.uk/developers/). Changes to code can be made by cloning the repo and pushing back or through the Github web interface. (or email!)

Programs for beginners are especially welcome.

Drop me an email if you have any ideas or want to get involved.

Carry on being amazing!
