Title: Making This Site, Part 3: Article Template
Date: 2017-02-04 21:36
Tags: programming, web-dev, pelican, jinja2

Welcome to the third installment of "Making This Site". In these articles I will describe the exact steps I went through to build this site. 

To view this post the way it looked by the end of making all the changes described in this article [click here]()

### A Basic Article Template

Let's start by adding `article.html` to our `templates` directory:

	$ touch theme/templates/article.html

Lets get a basic layout in place:

	{% extends "base.html" %}
	{% block title %}{{ article.title }} — {{ SITENAME }}{% endblock %}
	{% block content %}
	<h2 class="article-title">{{ article.title }}</h1>
	<div class="article-body">{{ article.content }}</div>
	{% endblock %}

Notice how we override the `title` block inherited from `base.html`

### Adding Metadata

I would like to add metadata to a line right beneath the title that contains the date of publication along with the the category and tags if they exist. The metadata for this post would look something like:

	Feb 04, 2017 / making-this-site / programming, web-dev, pelican

We can get all of this info from the `article` object provided by the template:

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

Does any of this code look familiar? It should it's almost the same as the code use for displaying of post metadata on the homepage.

#### Using Macros to Share Code

It is highly likely that I will always want to use the same style of printing metadata between the article and the home pages. Jinja2 lets you create a `macros.html` file in `templates` to hold common code.

	$ touch theme/templates/macros.html

Open `macros.html` and define the `get_meta_data_html` macro:

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

I have also updated `index.html` to use this code.

#### Title and Metadata Margins

With the changes we have made so far the metadata is separated from the article title by a big margin and there is no space between the metadata and the first line of the article. Let's user CSS to reverse this situation. Add the following to the "Default && Mobile" section of `jaredandrews.css`:

	.article-title {
		margin-bottom: 0rem;
	}

	.article-metadata {
		margin-bottom: 2rem;
	}

That's better!

### Showing Other Posts in a Category (With Plugins!)

One additional change I would like to add is navigation at the bottom articles that have categories to other articles in that category. This will allow someone to read this article and then go to the next article in the making-this-site category.

I discovered that this behavior is not easily achieved with the default behavior provided by Pelican. Luckily there is a [Pelican Plugin](https://github.com/getpelican/pelican-plugins) called [Neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors) which provides this functionality.

To include the Neighbors plugin I added code to `pelicanconf.py` specifying where plugins live in my repository and which plugin I wanted to use:

	PLUGIN_PATHS = ['plugins']
	PLUGINS = ['neighbors']

I also created the `plugins` directory and copied the code for Neighbors into it.

Neighbors adds functions for finding an articles neighbors. We use two of them below:

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

In a previous post I stated that I wouldn't use categories most of the time. I didn't realize at the time that all posts are assigned to the `DEFAULT_CATEGORY`. This is problematic for me as I don't want to show next/previous in category navigation for articles that don't belong to a Category I assigned them to.

In `pelicanconf.py` I defined a `DEFAULT_CATEGORY`:

    DEFAULT_CATEGORY = 'Unorganized'

Next I replaced instances of my mistaken check, `{% if article.category %}` with `{% if article.category != DEFAULT_CATEGORY %}`. I discovered another issue though, it appears that `macros.html` does not receive variables defined in `pelicanconf.py`. Thus I updated the `get_meta_data_html` macro to take a second argument, which is the default category.

### Wrapping Up

We now have our own Article template!

To see the complete code for the site at this point checkout COMMIT HASH LINK on GitHub.
