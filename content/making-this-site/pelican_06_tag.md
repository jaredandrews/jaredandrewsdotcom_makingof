Title: Making This Site, Part 6: Tag Templates
Date: 2017-02-22 11:36 
Tags: programming, web-dev, pelican, jinja2

There are only a couple templates we need for this to be a complete Pelican theme. Two of them are related to tags, `tag.html` and `tags.html`.

The `tag.html` template displays articles related to a specifc tag and the `tags.html` template displays a list of all tags on the site. Let's add these two templates.

### The Tag Template

For `tag.html` I just want to show the name of the tag and list related articles which is very similar to what we have done in `category.html` and `archives.html`.

	$ touch theme/templates/tag.html

Then we basically copy `category.html` and make a few changes:

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

`tag.html` gets a variable called `tag` which contains the name of the selected `tag`. I put this in the title block of the page and in the `h2` of the page. Like `category.html`, `tag.html` provides `articles` which contains a list of relevant articles.

With this new template clicking on tags in a posts metadata will take you to a fresh looking page instead of a blank page.

### The Tags Template

For `tags.html` I just want to list all the tags on the site along with a number indicating how many articles have the given tag.

	$ touch theme/templates/tags.html

`tags.html` is undocumented in the [Pelican 3.7.1 Docs](http://docs.getpelican.com/en/stable/themes.html) but the 'simple' theme shows [an example](https://github.com/getpelican/pelican/blob/master/pelican/themes/simple/templates/tags.html).

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

We have added `tag.html` and `tags.html` templates to the site. The only remaining template that I am interested in handling is `page.html` which will be addressed in the next post.

To see the complete code for the site at this point checkout COMMIT HASH LINK on GitHub.

To see what the site looked after these changes were made [click here]().
