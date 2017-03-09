Title: Making This Site, Part 6: Tag Templates
Date: 2017-02-22 11:36 
Tags: programming, web-dev, pelican, jinja2

There are only a couple templates left for this to be a complete Pelican theme. Two of them are related to tags, `tag.html` and `tags.html`.

The `tag.html` template displays articles related to a specifc tag and the `tags.html` template displays a list of all tags on the site.

### The Tag Template

For `tag.html` I just want to show the name of the tag and list related articles which is very similar to what I have done in `category.html` and `archives.html`.

	$ touch theme/templates/tag.html

I basically copied `category.html` and made a few changes:

	{% from 'macros.html' import get_article_list  %}
	{% extends "base.html" %}
	{% block title %}{{ tag }} — {{ SITENAME }}{% endblock %}
	{% block content %}
		<h2>Posts tagged with: {{ tag }}</h2>
		{{ get_article_list(articles, DEFAULT_CATEGORY) }}
		<p>
			<a href="{{ SITEURL }}/tags.html">Click here for a list of all tags.</a>
		</p>
	{% endblock %}

`tag.html` gets a variable called `tag` which contains the name of the
selected `tag`. I put this in the title block of the page and in the
`h2` of the page. Like `category.html`, `tag.html` provides `articles`
which contains a list of relevant articles.


### The Tags Template

For `tags.html` I just want to list all the tags on the site along
with a number indicating how many articles have the given tag.


	$ touch theme/templates/tags.html

`tags.html` is undocumented in the
[Pelican 3.7.1 Docs](http://docs.getpelican.com/en/stable/themes.html)
but the 'simple' theme shows
[an example](https://github.com/getpelican/pelican/blob/master/pelican/themes/simple/templates/tags.html).


    {% extends "base.html" %}
	{% block title %}Tags — {{ SITENAME }}{% endblock %}

	{% block content %}
		<h2>Tags</h2>
		<ul>
			{% for tag, articles in tags|sort %}
				<li><a href="{{ SITEURL }}/{{ tag.url }}">{{ tag }}</a> ({{ articles|count }})</li>
			{% endfor %}
		</ul>
	{% endblock %}

### Wrapping Up

I have added `tag.html` and `tags.html` templates to the site. The only remaining template that I am interested in handling is `page.html`.

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/06).

[Commit]() and [diff]() on GitHub.
 
