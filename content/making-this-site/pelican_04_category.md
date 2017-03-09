Title: Making This Site, Part 4: Category Template 
Date: 2017-02-07 21:36 
Tags: programming, web-dev, pelican, jinja2 

Now that I have an article template, I want to create a template for
the page that shows all articles that belong to the same category.

### The Category Template

`category.html` is a template for showing all the articles in a
specific category. For my purposes I would like to show the name of
the category, a description and a time ordered list of all the posts
associated with it.

Lets get started:

    $ touch theme/templates/category.html

Now I open up the new template and add some boilerplate:

    {% extends "base.html" %}
	{% block title %}{{ category }} — {{ SITENAME }}{% endblock %}
	{% block content %}
		<h2>{{ category }}</h2>
		<!-- TODO - content -->
	{% endblock %}

The category template has it's own [set of variables](http://docs.getpelican.com/en/stable/themes.html#category-html). Above I use the `category` variable to print the category name in both the `<title>` block and in the content of the page.

#### Listing Articles in a Category

I want to list the articles in a category in the same way that I do on
the home page. This opens up another codesharing opportunity, I took
the the article listing code from `index.html`, and modified it in
`macros.html`:

	{% macro get_article_list(articles, default_category) %}
		<ul>
			{% for article in articles %}
				<li>
					<a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a>
					&nbsp
					<span class="post-meta">({{ get_meta_data_html(article, default_category) }})</span>
				</li>
			{% endfor %}
		</ul>
	{% endmacro %}

Because of the dependence on the `get_meta_data_html` macro I also
pass `DEFAULT_CATEGORY` to `get_article_list`. To make use of this new
macro, I added:

	{% from 'macros.html' import get_article_list  %}

to the top of the templated. Then, I replaced `<!-- TODO - content --> with:

	{{ get_article_list(articles, DEFAULT_CATEGORY) }}

`articles` is another template variable that provides a list of articles associated with a category.

#### Adding a Category Description With category_meta

At this point the category page is almost exactly how I want it. The
only other thing I desire is a description of the category which will
be printed above the list of articles. A category description is not
supported by Pelican out of the box.

With a quick Google search I found the
[category_meta](https://github.com/getpelican/pelican-plugins/tree/master/category_meta)
plugin which allegedly provides a way to add a description to a
Category.

#### Setting Up category_meta
I copied the `category_meta` project into my `plugins` folder.

`category_meta` calls for posts to be organized such that there is a
directory for each category and all the posts associated with that
category are in that directory. Thus my `content` folder went from
looking like this:

    content
    ├── pelican_00_setup.md
    ├── pelican_01_base.md
    ├── pelican_02_index.md
    └── pelican_03_article.md

to:

	content
	└── making-this-site
	     ├── pelican_00_setup.md
	     ├── pelican_01_base.md
	     ├── pelican_02_index.md
	     ├── pelican_03_article.md
         └── pelican_04_category.md

The name of this new directory is also what is used for the category page slug. Thus the categeory page for "Making My Site" will be `categories/making-this-site.html`.

`category_meta` also specifies that every category folder contains an `index.md`, this file holds the metadata for the category:

	Title: Making This Site

	A flow of conscious tutorial describing, in excruciating detail, how this site was made.

Going back to `category.html` I can show the description underneath the title with:

	<p>{{ category.description }}</p>

The documentation also says to remove the category key from posts, so I did that as well.

Now I should have category descriptions!

##### Time For a Side Quest: Fixing The category_meta Plugin

After adding all the `category_meta` related files I went and ran `./develop_server start`. The site compiled and I went to check out my sweet new category page. Everything looked good but my category description was missing!

I went back and looked at the output of `develop_server` and saw:

	ERROR: Skipping category/index.md: could not find information about 'date'
	ERROR: No category assignment for ~/pelican_category_meta_problems/content/category/post.md (~/pelican_category_meta_problems/content/category/post.md)

Hmm okay... It didn't really make sense but I went ahead and added a date to `making-this-site/index.md`.

	Date: 2015-11-01 10:02

Building the again a new error appeared:

	CRITICAL: AttributeError: can't set attribute

Since I have the source of the plugin in my repo I was able to trace
this warning back into the `category_meta` plugin. In
`plugins/category_meta/category_meta.py` on line 73, there is this
piece of code:

    category.slug = slug

First I just commented it out. This change got my category description
to appear but I didn't feel good about it, obviously that line was
there for a reason, right?!

From what I can tell the purpose of that line is to set the categories
slug to the name of the categories directory name. Line 73 is part of
the function `make_category(article, slug)`, and indeed, it is called
in `pretaxonomy_hook` function like this:

	make_category(article, os.path.basename(dirname))

By removing line 73 I would lose the ability to set the category slug
based on the directory and I'm not even sure how the category slug
would be generated. I didn't go into the Pelican source enough but
from what I can tell it took the name of the category and snakecased.

So what could have caused this issue? At the time of writing this
article I am using the newest vesrion of Pelican, `3.7.1`. My guess
woulld be that at some point `category.slug` was mutable and in this
version it is not. I inspected the `category` object to see if I could
edit the slug in another way. Running `dir(category)` revealed that
there was another member of `category` called `_slug`, so I changed
line 73 to:

	category._slug = slug

This fixed the issue! BUT I had now modified the plugin to access
what, by Python convention, is supposed to be a private variable. The
danger in doing this is that the variable could disappear or change
next time I upgrade Pelican.

This made me feel bad but I have a website to build! I documented
and reported the issue to
[pelican-plugins on GitHub](https://github.com/getpelican/pelican-plugins),
you can see the issue
[here](https://github.com/getpelican/pelican-plugins/issues/855). Hopefully,
by the time this article is published there will be a cleaner solution
than what I have done above.

### Wrapping Up

I now have a category template!

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/04).

[Commit](https://github.com/jaredandrews/jaredandrewsdotcom_makingof/commit/575951007462514058cbcb171f2286ebcbbc147a) on GitHub.
  
