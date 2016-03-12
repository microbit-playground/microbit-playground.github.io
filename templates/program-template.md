---

title: A Template for Micro:bit Projects
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "A catchy except is for in teasers and the description for Google."

# exact sizes to match your project. PNG or JPG.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter.png
# Resides in /images/ folder
image:
  feature: YYYY-MM-DD-project-name-featured.svg
  teaser: YYYY-MM-DD-project-name-teaser.png # or .gif or .jpg
  credit: Optional image credit to comply with CC licences
  creditlink: http://link.com

# edit /data/author.yml with your details for info box. Please consider attributing your contribution to inspire kids.
# the author box contains links to twitter/websites etc

author: jez_dean

# Add only if project is updated after publication. 2016-12-25
modified:

shareable: yes


---

This is the _kitchen sink_ of templates. I've added every possible thing. Use this if you want amazing documentation for your contributed project.

As you can see, the first paragraph is larger so I've made it snappy.

You don't have to add all this fancy stuff[^footnote]. If you want, submit just bare documentation please use [the bare template.](program-template-bare.md) If you do use `template-bare.md` please submit a few photos with pull request; I'll type them up into a project.

[^footnote]: But if you write it up, I will love you forever.


---

## Check List

* Name documentation `YYYY-MM-DD-my-tile.md`.
* Name code `YYYY-MM--DD-my-title.py`.
* Put code and documentation into `/programs/`
* Images in `/images/` following `YYYY-MM-DD-my-title-1.jpg`
* And include your code at the bottom of your documentation.

#### Include your code at the bottom of the documentation:

<pre>
&#123;% highlight python %&#124;

&#123;% include_relative 2016-01-16-my-python-code.py %&#124;

&#123;% endhighlight %&#123;
</pre>


---

## Table of Contents

If you have a really big project you'll need a Table of Contents. You don't have to use one; it's not even preferred.

{% include toc.html %}

H2 `##` should be used for each main section and H3 `###` for subsections. H3 headers do not appear in the TOC.

If you need them, you can use H1 `#`; this gives more padding when appearing in the TOC.


---


## Feature Image & Thumbnail

Each post requires a teaser and a feature image.

### Feature (header) Image


Edit `/templates/program-template-header.svg`.

{% highlight html %}

<tspan x="0" y="80">
MY</tspan><tspan x="0" y="169">
MICROBIT</tspan><tspan x="0" y="258">
PROJECT</tspan>

{% endhighlight %}

Edit the lines with your project name.

### Teaser Image

180px x 110px image of your code.

This site would be rather boring if there were 100s of pictures of static Micro:bits! Here are some examples of photos for imaginary projects:

| Micro:bit Project        | Examples of Photos to Illustrate           |
| ------------- |:--------------|
| Morse code generator      | Photograph of Morse code key |
| Basketball Score Keeper      | Photograph of people playing basket ball, or picture of  the Micro:bit being used      |
| Fortune Cookie Game | A photograph of a fortune cookie, or a drawing of the Micro:bit in the shape of a fortune cookie      |

Please comply with copyright (we have to model good behaviour!)

---

## Code Highlighting

To do whole blocks, use `% highlight ruby %` and it looks like this.

{% highlight ruby %}

puts 'Hello, I'm highlighted Ruby!'

{% endhighlight %}

Remember to specify the language in your project. Here's Java:

{% highlight java %}

class HelloWorld {
  static public void main( String args[] ) {
    System.out.println( "I'm jealous of Ruby!" );
  }
}

{% endhighlight %}

Dead easy, or use the `the markdown standard with backticks`.

---


## Images

### Images in Markdown

Adding images in Markdown is really easy.

#### Four Images side-by-size
![an embedded image](https://placehold.it/180x200) ![an embedded image](https://placehold.it/180x200) ![an embedded image](https://placehold.it/180x200) ![an imbedded image](https://placehold.it/180x200)


#### Single whole width
![an imbedded image](https://placehold.it/800x200)

### Images in HTML

Adding images in HTML allows you more options. I'd love this to be in native Markdown but this is the best I can do.

If you want to display two or three images next to each other responsively use `figure` with `full`, `half` or `third`. Each instance of `figure` is auto-numbered and displayed in the caption.


#### Using 'half' class with Caption
<figure class="half">
	<img src="https://placehold.it/800x200">
	<img src="https://placehold.it/800x200">
	<figcaption>Caption describing these two images.</figcaption>
</figure>

#### Using 'third' Class with Caption
<figure class="third">
    <img src="https://placehold.it/800x200">
    <img src="https://placehold.it/800x200">
    <img src="https://placehold.it/800x200">
	<figcaption>Caption describing these three images.</figcaption>
</figure>

### Naming Images

<figure class="pull-right">
  <img src="https://placehold.it/200x200" alt="Right">
  <figcaption>Images can float right.</figcaption>
</figure>

You can float images out of the way with `class="pull-right"`.

Image names follow this convention:

* `YYYY-MM-DD-name-of-article-illustration-1.jpg`
* `YYYY-MM-DD-name-of-article-illustration-2.gif`
* `YYYY-MM-DD-name-of-article-illustration-3.png`
* `YYYY-MM-DD-name-of-article-illustration-4.jpg`
* `YYYY-MM-DD-name-of-article-feature.svg`
* `YYYY-MM-DD-name-of-article-teaser.jpg`

---

## Videos

<iframe width="560" height="315" src="//www.youtube.com/embed/9e1nPyHXCFQ" frameborder="0"> </iframe>

Easy to add! Will appear full width. Vines work too.

---

Blockquote

> Do people who wave at trains / Wave at the driver, or at the train itself?



> <cite>Roger McGough, *Waving at Trains*</cite>

---

## Authors

It's easy to add an author box to your project. Open `/_data/authors.yml` and add in your information:

{% highlight yaml %}
# Filename: /_data/authors.yml

jez_dean:
  name: Jez Dean
  web: http://geekteacher.co.uk
  email: jez@geekteacher.co.uk
  bio: "This is a bio. Inspire and captivate the learner."
  avatar: bio-photo.jpg
  twitter: jezMr

{% endhighlight %}

Add this to the head of your project's `.md` file.

{% highlight yaml %}

author: jez_dean

{% endhighlight %}

Adding an author box shows kids _real_ coders. It's inspirational. It's _really_, ___really___ important if you happen to be female.

---

## Buttons

Applying `.btn'` class to a link makes a button, eg `<a href="#" class="btn">`.


<a href="#" class="btn">.btn</a>
<a href="#" class="btn-inverse">.btn-inverse</a>
<a href="#" class="btn-info">.btn-info</a>
<a href="#" class="btn-warning">.btn-warning</a>
<a href="#" class="btn-danger">.btn-danger</a>
<a href="#" class="btn-success">.btn-success</a>

### Social Media Buttons

<a href="#" class="btn-social facebook"><i class="fa fa-facebook" aria-hidden="true"></i> Facebook</a>
<a href="#" class="btn-social flickr"><i class="fa fa-flickr" aria-hidden="true"></i> Flickr</a>
<a href="#" class="btn-social foursquare"><i class="fa fa-foursquare" aria-hidden="true"></i> Foursquare</a>
<a href="#" class="btn-social google-plus"><i class="fa fa-google-plus" aria-hidden="true"></i> Google+</a>
<a href="#" class="btn-social instagram"><i class="fa fa-instagram" aria-hidden="true"></i> Instagram</a>
<a href="#" class="btn-social linkedin"><i class="fa fa-linkedin" aria-hidden="true"></i> LinkedIn</a>
<a href="#" class="btn-social pinterest"><i class="fa fa-pinterest" aria-hidden="true"></i> Pinterest</a>
<a href="#" class="btn-social rss"><i class="fa fa-rss" aria-hidden="true"></i> RSS</a>
<a href="#" class="btn-social tumblr"><i class="fa fa-tumblr" aria-hidden="true"></i> Tumblr</a>
<a href="#" class="btn-social twitter"><i class="fa fa-twitter" aria-hidden="true"></i> Twitter</a>
<a href="#" class="btn-social vimeo"><i class="fa fa-vimeo-square" aria-hidden="true"></i> Vimeo</a>
<a href="#" class="btn-social youtube"><i class="fa fa-youtube" aria-hidden="true"></i> YouTube</a>

Font Awesome is in there so there's hundreds of icons to choose from.

---

## Boxes

<div class="notice-success">
	<h3>Headline</h3>
    <p>I'm just a little bit of text.</p>
	<div class="inline-btn">
		<a href="#" class="btn-social instagram"><i class="fa fa-instagram" aria-hidden="true"></i> Instagram</a>
		<a href="#" class="btn-social linkedin"><i class="fa fa-linkedin" aria-hidden="true"></i> LinkedIn</a>
        <a href="#" class="btn-social foursquare"><i class="fa fa-foursquare" aria-hidden="true"></i> Foursquare</a>

	</div><!-- /.inline-btn -->
</div>

---

### Info Boxes

**Look How Simple:** Just put `{: .notice-warning}` on a new line after the paragraph you've written.
{: .notice-success}

**Info Notice:** `.notice-info` [Maecenas ornare tortor](). Donec sed tellus eget sapien fringilla nonummy. Mauris a ante. Suspendisse quam sem, consequat at.
{: .notice-info}

**Inverse Notice:** `.notice-inverse` Maecenas ornare tortor. Donec sed tellus [eget sapien fringilla]() nonummy. Mauris a ante. Suspendisse quam sem, consequat at.
{: .notice-inverse}

**Warning Notice:** `.notice-warning` Maecenas ornare tortor. Donec sed [tellus eget]() sapien fringilla nonummy. Mauris a ante. Suspendisse quam sem, consequat at.
{: .notice-warning}

**Danger Notice:** `.notice-danger` Maecenas ornare tortor.[ Donec sed tellus]() eget sapien fringilla nonummy. Mauris a ante. Suspendisse quam sem, consequat at.
{: .notice-danger}

**Success Notice:** `.notice-success` Maecenas ornare tortor. Donec sed tellus eget [sapien fringilla]() nonummy. Mauris a ante. Suspendisse quam sem, consequat at.
{: .notice-success}

---

## Forms

---

You'll never need these but hey...


<fieldset>
	<form>
		<h2>Join the Mailing List</h2>
		<p>Once a fortnight receive information on micro:bit happenings.</p>
		<label for="text_field">Text Field:</label>
		<input type="text" id="text_field" />
		<label for="text_area">Text Area:</label>
		<textarea id="text_area"></textarea>
		<p>
			<label for="select_element">Select Element:</label>
			<select name="select_element">
				<optgroup label="Option Group 1">
					<option value="1">Option 1</option>
					<option value="2">Option 2</option>
					<option value="3">Option 3</option>
				</optgroup>
				<optgroup label="Option Group 2">
					<option value="1">Option 1</option>
					<option value="2">Option 2</option>
					<option value="3">Option 3</option>
				</optgroup>
			</select>
		</p>
		<p>
			<label for="radio_buttons">Radio Buttons:</label>
			<label><input type="radio" class="radio" name="radio_button" value="radio_1" />Radio 1</label>
			<label><input type="radio" class="radio" name="radio_button" value="radio_2" />Radio 2</label>
			<label><input type="radio" class="radio" name="radio_button" value="radio_3" />Radio 3</label>
		</p>
		<p>
			<label for="checkboxes">Checkboxes:</label>
			<label><input type="checkbox" class="checkbox" name="checkboxes" value="check_1" />Checkbox 1</label>
			<label><input type="checkbox" class="checkbox" name="checkboxes" value="check_2" />Checkbox 2</label>
			<label><input type="checkbox" class="checkbox" name="checkboxes" value="check_3" />Checkbox 3</label>
		</p>
		<p>
			<label for="password">Password:</label>
			<input type="password" class="password" name="password" />
		</p>
		<p>
			<label for="file">File Input:</label>
			<input type="file" class="file" name="file" />
		</p>
		<p>
			<input class="btn" type="submit" value="Submit" />
		</p>
	</form>
</fieldset>

---

### Program Header Image

![header images](/templates/program-template-header.svg)

Each program listed has its own write up in an `.md` file. It also has a `.svg` file. This is just a text file. Up to three lines
of text can be added. Take a look at the code of the image above:

{% highlight html %}

<svg xmlns="http://www.w3.org/2000/svg" width="850" height="400">
  <path fill="darkorchid" d="M0 0h850v400H0V0z"/>
  <path fill="#FFF" d="M358.622-39.934l516.82 91.13-65.536 371.67-516.82-91.128 65.536-371.672z"/>
  <text stroke-width="0" stroke-miterlimit="3" transform="rotate(10 182.54 2159.47)" font-family="Arial" font-size="80">
    <tspan x="0" y="80">
Press</tspan>
            <tspan x="0" y="169">
the</tspan>
            <tspan x="0" y="258">
Button</tspan>


            </text>
</svg>

{% endhighlight %}

---

## Vine videos are easy to embed too!

<iframe src="https://vine.co/v/irwjB70Adq1/embed/simple" width="300" height="300" frameborder="0" style="float: right"></iframe><script src="https://platform.vine.co/static/scripts/embed.js"></script>

---

## I'm Concerned...

... that this will put you off pushing up code! This guided was written mainly for me to use when editing pull requests.

It's is _fine_ to submit a few photos and basic documentation; I'll do the rest.

Again, please: do not be put off!

---
