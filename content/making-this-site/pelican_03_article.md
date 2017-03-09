Title: Making This Site, Part 3: Article Template
Date: 2017-02-04 21:36
Tags: programming, web-dev, pelican, jinja2

Now I want to create the article template. This template controls the
look of articles like this one.

### A Basic Article Template

First I add the article template file:

	$ touch theme/templates/article.html

Then, a very basic article template:

	{% extends "base.html" %}
	{% block title %}{{ article.title }} — {{ SITENAME }}{% endblock %}
	{% block content %}
	<h2 class="article-title">{{ article.title }}</h1>
	<div class="article-body">{{ article.content }}</div>
	{% endblock %}

The `title` block inherited from `base.html` is overridden to show the
name of the article in the title bar.

### Adding Metadata

I would like to add metadata to a line right beneath the title that
contains the date of publication along with the the category and tags
if they exist. This article would have metadata looking something like:

	Feb 04, 2017 / making-this-site / programming, web-dev, pelican

All of this info can be pulled from the  `article` object provided by the template:

    <footer class="article-metadata">
      {{ article.date.strftime('%b %d, %Y') }}
      {% if article.category %}
        / <a href="article.category.url">{{ article.category }}</a>
      {% endif %}
      {% if article.tags %}
        /
        {% for tag in article.tags %}
          {% if not loop.last %}
            <a href="{{ SITEURL }}/{{ tag.url }}" rel="tag">{{ tag }}</a>,
          {% else %}
            <a href="{{ SITEURL }}/{{ tag.url }}" rel="tag">{{ tag }}</a>
          {% endif %}
        {% endfor %}
      {% endif %}
    </footer>

This is almost the same as the code used to show article metadata on
the front page.

#### Using Macros to Share Code

It is highly likely that I will always want to use the same style of
printing metadata between the article and the home pages. Jinja2 lets
me create a `macros.html` file in `templates` to hold common code.

	$ touch theme/templates/macros.html

I created a macro named `get_meta_data_html` to print metadata for a
given article:

    {% macro get_meta_data_html(article) %}
      {{ article.date.strftime('%b %d, %Y') }}
      {% if article.category %}
      / <a href="{{ SITEURL }}/{{ article.category.url }}">{{ article.category }}</a>
      {% endif %}
      {% if article.tags %}
        /
        {% for tag in article.tags %}
          {% if not loop.last %}
            <a href="{{ SITEURL }}/{{ tag.url }}" rel="tag">{{ tag }}</a>,
          {% else %}
            <a href="{{ SITEURL }}/{{ tag.url }}" rel="tag">{{ tag }}</a>
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endmacro %}

This macro takes an article and then provides the metadata html for it.

Now the `footer` in `article.html` looks like this:

    <footer class="article-metadata">
      {{ get_meta_data_html(article) }}
    </footer>

I have also updated `index.html` to use this macro.

#### Title and Metadata Margins

With the changes I have made so far the metadata is separated from the
article title by a big margin and there is no space between the
metadata and the first line of the article. To reverse this situation
I added the following to the "Default && Mobile" section of
`jaredandrews.css`:

	.article-title {
		margin-bottom: 0rem;
	}

	.article-metadata {
		margin-bottom: 2rem;
	}

Nice!

### Showing Other Posts in a Category (With Plugins!)

I would like to add navigation at the bottom of 
articles linking to other articles that share the same category.
This will allow someone to read this article and then go to the next
article in the `making-this-site` category.

I discovered that this behavior is not easily achieved out of the
box. Luckily there is a
[Pelican Plugin](https://github.com/getpelican/pelican-plugins) called
[Neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
which provides this functionality.

To include the Neighbors plugin I added code to `pelicanconf.py` specifying where plugins live in my repository and which plugins I wanted to use:

	PLUGIN_PATHS = ['plugins']
	PLUGINS = ['neighbors']

I also created the `plugins` directory and copied the code for Neighbors into it.

Neighbors provides functions for finding an articles neighbors. I use two of them below:

    {% if article.category %}
    <div class="row"> 
      {% if article.prev_article_in_category %}
      <span style="float:left">
        &#8592;
        <a href="{{ SITEURL }}/{{ article.prev_article_in_category.url}}">
          {{ article.prev_article_in_category.title }}
        </a>
      </span>
      {% endif %}
    
      {% if article.next_article_in_category %}
      <span style="float:right">
        <a href="{{ SITEURL }}/{{ article.next_article_in_category.url}}">
          {{ article.next_article_in_category.title }}
        </a>
        &#8594;
      </span>
      {% endif %}
    </div>
    {% endif %}

This creates "next" and "previous" article buttons at the bottom of an article if it has a category.

#### But Wait There's A Problem

In a previous post I stated that I wouldn't use categories most of the
time. I didn't realize at the time that all posts are assigned to the
`DEFAULT_CATEGORY`. This is problematic for me as I don't want to show
next/previous in category navigation for articles that don't belong to
a Category I assigned them to.


In `pelicanconf.py` I defined a `DEFAULT_CATEGORY`:

    DEFAULT_CATEGORY = 'Unorganized'

Next I replaced instances of my mistaken check, `{% if
article.category %}` with `{% if article.category != DEFAULT_CATEGORY
%}`. I discovered another issue though, it appears that `macros.html`
does not receive variables defined in `pelicanconf.py`. So I updated
the `get_meta_data_html` macro to take a second argument, which is the
default category.

### Wrapping Up

I now have an Article template!

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/03).

[Commit]() and [diff]() on GitHub.
  
