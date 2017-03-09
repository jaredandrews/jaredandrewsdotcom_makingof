Title: Making This Site, Part 5: Archive Template 
Date: 2017-02-20 19:08
Tags: programming, web-dev, pelican, jinja2

Now I am going to add the `archives.html`  template to the theme.

Curiously, the
[Pelican 3.7.1 documentation](http://docs.getpelican.com/en/stable/themes.html)
mentions `archives.html` but does not document what variables are
available. Fortunately, the Pelican "simple" theme has an
[`archives.html`](https://github.com/getpelican/pelican/blob/master/pelican/themes/simple/templates/archives.html):


	{% extends "base.html" %}
    {% block content %}
    <h1>Archives for {{ SITENAME }}</h1>
    
    <dl>
    {% for article in dates %}
        <dt>{{ article.locale_date }}</dt>
        <dd><a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a></dd>
    {% endfor %}
    </dl>

It looks like `archives.html` has a `dates` variable which contains a
list of articles. This is different than `index.html` and
`category.html` which provide a list of articles named `articles`.

### A Basic Archives Template

	$ touch theme/templates/archives.html

To start, I want `archives.html` to be nearly identical `index.html`:

	{% from 'macros.html' import get_article_list  %}
	{% extends "base.html" %}
	<h2>Archive</h2>
	{% block content %}
	{{ get_article_list(dates, DEFAULT_CATEGORY) }}
	{% endblock content %}

Next I update `base.html` so that the "archive" link in the nav menu
goes to the right place:

	<a href="{{ SITEURL }}/archives.html">archive</a> 

### Handling External Links

I frequently contribute to other websites. I wanted to
have a list of links on *this site*  that went to outside urls. I also
wanted to be able to tag these external links using the same tagging
system being used for posts on this site. But I didn't want my
external work to clog up the archives for this this site.

So I added a new category named `external-links`

	$ mkdir content/external-links
    $ touch content/external-links/index.md

Content of `content/external-links/index.md`:

	Title: External Links 
	Date: 2015-11-01 10:02 

	A list of things I have been involved with that are hosted on other websites.

	The links included here are mostly focused on my involvement with [Spark & Fizz](https://sparkandfizz.com) and the greater DIY music community. If you are interested in seeing Software Development projects I have been involved with, please take a look at my [LinkedIn profile](https://www.linkedin.com/in/jaredtandrews). 

	The tags you see next to these posts typically describe the nature of my involvment. 

I added my first post to the category as well:

	$ touch content/external-links/boston_zine_fest.md

And wrote:

	Title: Spark & Fizz Goes to Boston Zine Fest 2015
	Date: 2015-10-17 10:02
	Tags: spark-and-fizz, cameraman, video-editing, interviewer
	Link: http://www.sparkandfizz.com/blog/2015/10/17/spark-fizz-goes-to-boston-zine-fest-2015

Notice the lack on content and the new `Link` key. For this to work I
need to specifically handle posts with a category of `External Links`,
if they have that category I would like to extract the `Link` value
and use it.

Opening up `macros.html` again, let's change the previously defined `get_article_list` function to handle external links:

	{% if article.category.name == 'External Links' %}
	<a href="{{ article['link'] }}" target="_blank">{{ article.title }}</a>
	{% else %}
	<a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a>
	{% endif %}

An `if` statement was added and I check for the `External Links`
category. If a post has that category I open the link provided by
`article['link']` in a new a tab. Notice that Pelican automatically
added the link attribute to `article`.


I am not very familiar with the Pelican codebase and I couldn't find
any documention about what would happen when adding new keys to a post
such as `Link` above. I'm not sure if what I am doing here is totally
misguided or not. Something I noticed was that I even though I
declared `Link` in the markdown for the post I could only access it
via `article['link']`, the case was dropped. I'm not sure why this is.

As I said I didn't want to show external links in the archive or the
list on my homepage. Since all those places use the same
`get_article_list` method to display post information I made a
modification to that:

    {% macro get_article_list(articles, default_category, hidden_category) %}
        <ul>
            {% for article in articles %}
                {% if article.category.name != hidden_category %}
                    <li>
						{% if article.category.name == 'External Links' %}
                	        <a href="{{ article['link'] }}" target="_blank">{{ article.title }}</a>
						{% else %}
							<a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a>
						{% endif %}
						&nbsp
						<span class="post-meta">({{ get_meta_data_html(article, default_category) }})</span>
					</li>
                {% endif %}
            {% endfor %}
        </ul>
    {% endmacro %}

Basically if the caller of this method indicates a `hidden_category`,
articles matching that category will be left out.

Now if I when I access
[http://localhost:8000/category/external-links.html](http://localhost:8000/category/external-links.html)
I can see a list of just the external links, `category.html` is
handling this display and it passes no `hidden_category` to
`get_article_list`.

I also added a link to the top of `archive.html` that goes directly to
that page:

	<p>
		This page shows and archives of posts to this site. If you would like to see contributions I have made to outside sources [click here]({{ SITEURL }}/category/external-links.html)
	</p>

### Making Embedded Code Look Better

I am saving most of my design refinement for after the site is
complete. But as I proofread these posts the way the embedded looks
frustrates me. So I am changing it now. There is apparently a way to
display code snippets with [Pygments](http://pygments.org/). I might
try to use Pygments in the future, it looks cool but for now I was
really only peeved by the indenting of the code. I modified
`theme/static/jaredandrews.css` with:

	.highlight {
		padding: 0 1.5em 0 1.5em;
	}

This made the code distinct enough from the body text.

### Wrapping Up

NowI  have an Archive page that can be accessed from the nav menu.

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/05).

[Commit](https://github.com/jaredandrews/jaredandrewsdotcom_makingof/commit/d3f6803222e1d76ac31f1a74e75e537f9e027833) on GitHub.

 



