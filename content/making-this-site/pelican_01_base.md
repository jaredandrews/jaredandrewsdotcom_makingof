Title: Making This Site, Part 1: Base Template
Date: 2015-11-03 19:00
Tags: programming, web-dev, pelican, skeleton, jinja2

Welcome to the first installment of "Making This Site". In these articles I will describe the exact steps I went through to build this site. 

To view this post the way it looked by the end of making all the changes described in this article [click here]()

### Cleaning the Config

Each Pelican project has ```pelicanconf.py``` file that described site
wide metadata. The ```pelican-quickstart``` tool used in the previous
entry to create the skeleton for this site generates a conf file with
sensible defaults:

    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals
    
    AUTHOR = u'Jared Andrews'
    SITENAME = u'Jared Andrews'
    SITEURL = 'http://localhost:8000'
    
    PATH = 'content'
    
    TIMEZONE = 'America/New_York'
    
    DEFAULT_LANG = u'en'
    
    # Feed generation is usually not desired when developing
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None
    
    # Blogroll
    LINKS = (('Pelican', 'http://getpelican.com/'),
             ('Python.org', 'http://python.org/'),
             ('Jinja2', 'http://jinja.pocoo.org/'),
             ('You can modify those links in your config file', '#'),)
    
    # Social widget
    SOCIAL = (('You can add links in your config file', '#'),
              ('Another social link', '#'),)
    
    DEFAULT_PAGINATION = False
    
    # Uncomment following line if you want document-relative URLs when developing
    #RELATIVE_URLS = True

Many of the keys directly map to the questions posed by
```pelican-quickstart```. The keys ```LINKS``` and ```SOCIAL``` are
not needed for my purposes so I have removed them. Once they are
removed you will notice that the sections containing them disapear
from the generated site. I also updated my `SITEURL` to point to
localhost. We will need to make this adjustable at some point when we
make this site deployable.

### Getting Started on a Custom Theme

To create a custom theme for Pelican you must create a directory for
your theme that has three directories, `static`,
`templates` and `css`. From the root of your Pelican project:

	$ mkdir -p theme/templates
	$ mkdir -p theme/static/css

Once you have created these directories open your `pelicanconf`
and add the following line:

    THEME='theme'

If you generate the site again at this point, y ou will notice it is
themeless and composed entired of text and basic HTML with no
style. From here we will develop our own theme.

### The Structure of a Theme

Themes in Pelican are created with templates using [language syntax]
that live in teh `theme/templates` directory. The structure of the
`templates` directory can be found in the
[Pelican Docs](http://docs.getpelican.com/en/3.6.3/themes.html).

We will start with `base.html` which provides the scaffolding for
all other templates in a theme.

    $ touch theme/templates/base.html

### Designing Base.html

As noted in [Part 0](/making-this-site-part-0-setup.html) of this
series I want the layout of my site to be extremely simple.

For the header of the site, which will be the primary component
provided by `base.html` I was only interested in displaying my name
and navigation.

The basic design I came up with looks like this:

![Sketch of Header Design](/images/rough_design.jpg)

#### A Quick Aside on Adding Images to Posts

As I use more Markdown tags in these posts I will try to remember
to point them out. You can add an image to a markdown file with:

	![Alt Text](/path/to/image)

To get pelican to include your images in it's output create a
directory in `content` called `images` and add the following line to
your `pelicanconf.py`:

    STATIC_PATHS = ['images']

#### Defining base.html

Since `base.html` will be extended by all other templates I need
to include the `html`, `head` and `body` tags. Let's start
by looking at the `head` tag and its contents:

    <!DOCTYPE html>
	<html lang="{{ DEFAULT_LANG }}">
		<head>
			<meta charset="utf-8">
			<title>{% block title %}{{ SITENAME }}{% endblock %}</title>

            <meta name="description" content="{% block description %}Personal site of Jared Andrews{% endblock %}">
			<meta name="author" content="{{ AUTHOR }}">
			<meta name="viewport" content="width=device-width,initial-scale=1.0">

	        <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">

	        <link rel="stylesheet" href="{{ SITEURL }}/theme/css/normalize.css" type="text/css">
			<link rel="stylesheet" href="{{ SITEURL }}/theme/css/skeleton.css" type="text/css">
			<link rel="stylesheet" href="{{ SITEURL }}/theme/css/jaredandrews.css" type="text/css">
		</head>
		<body>
			<!-- TODO -->
		</body>
	</html> 

The first thing you might notice about this code are blocks like `{{
SITENAME }}` and `{% endblock %}`. Pelican uses the
[Jinja2 Templating Engine](http://jinja.pocoo.org/) for templating.

Jinja2 provides a
[DSL for defining templates](http://jinja.pocoo.org/docs/2.9/templates/)
in a python-like language. Pelican provides
[a list of variables that can be accessed for each templated page](http://docs.getpelican.com/en/3.6.3/themes.html). Variables
defined in `pelicanconf.py` can also be accessed by any template.

Some important parts from above:

	<title>{% block title %}{{ SITENAME }}{% endblock %}</title>

`{{ SITENAME }}` prints the `SITENAME` defined in `pelicanconf.py`. By
surround `{{ SITENAME }}` with `{% block title %} ... {% endblock %}`
I am allowing child templates to override the content of `{% block
title %}`. This will become important when defining the child pages
where I don't want the `<title>` to just be the name of this site.

	        <link rel="stylesheet" href="{{ SITEURL }}/theme/css/normalize.css" type="text/css">
			<link rel="stylesheet" href="{{ SITEURL }}/theme/css/skeleton.css" type="text/css">
			<link rel="stylesheet" href="{{ SITEURL }}/theme/css/jaredandrews.css" type="text/css">

The above code imports a few css files from my `theme/assets/css`
directory.

I am using [Skeleton](http://getskeleton.com/) as the only css
"framework" for this project. Skeleton provides a nice set of
responsive styles for desktop and mobile. Skeleton asks that you
import `normalize.css` as well. If you are not familiar with this file
it basically sets the defautl values for all css elements so you are
working with a consistent base across browsers.

Then there is `jaredandrews.css`, this is the file I will put any
additional css I code I need in. We will look at this file again
later.

Now lets add the content of `<body>` which looks like this:

	<div class="container">

	    <div class="row header">
		    <h1 class="site-title"><a href="{{ SITEURL }}">Jared Andrews</a></h1>
     		<nav><a href="#">about</a> / <a href="#">archive</a> / <a href="#">rss</a></nav>
		</div>

        <div class="row">
			{% block content %}{% endblock %}
		</div>

	</div>

The first `<div>` has the class of `container`. This is the root
element for a Skeleton layout. Skeleton will center this div on the
page.

The second `<div>` has a class of `row` and `header`. `row` is another
class provided by Skeleton. It basically indicates that the selected
`<div>` lives on a row in the Skeleton grid. `header` is the class
that I will use to define the movement of the title and navigation
between mobile and desktop.

#### Using CSS to Adjust the Header

Let's start with a basic template for `jaredandrews.css`:

	/* Default and mobile */

	/* Larger than mobile */
	@media (min-width: 400px) {}

	/* Larger than phablet */
	@media (min-width: 550px) {}

	/* Larger than tablet */
	@media (min-width: 750px) {}

	/* Larger than desktop */
	@media (min-width: 1000px) {}

	/* Larger than Desktop HD */
	@media (min-width: 1200px) {}

Skeleton recommends using this set of media queries in your cusotm
css. Anything defined outside of a media query will both be the
default css for an element and what you see on mobile. Media queries
are then provided for larger screens.

Let's start with default/mobile:

	.header nav {
		display: block;
		text-align: center;
	}

	.header .site-title {
		margin: auto;
		text-align: center;
	}

These selectors center both elements and put the title above the
navigation.

After I define behavior for "larger than tablet" queries. The decision
to break here was based on my own testing with different screen
sizes. I left that the desktop layout looked best starting at this point.

	/* Larger than tablet */
	@media (min-width: 750px) {
		.header .site-title {
			float: left;
		}

	    .header nav {
			display: inline;
			float: right;
		}
	}

Now the layout of the header will react to the type of device it is
being views on.

### Wrapping Up

At this point we have a pretty nice looking site. Of course we will be
tweaking everything else, but just by providing the `base.html`
template we are able to make a lot of big changes to the way the site looks.

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/01).

[Commit]() and [diff]() on GitHub.
