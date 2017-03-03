Title: Making This Site, Part 2: Index Template
Date: 2017-02-04 19:00
Tags: programming, web-dev, pelican

Welcome to the second installment of "Making This Site". In these articles I will describe the exact steps I went through to build this site. 

To view this post the way it looked by the end of making all the changes described in this article [click here]()

### Designing the Home Page

In keeping with the overall "minimalist" vibe I only want my
home page to be a list of posts. Right now,
with the default template provided by Pelican, there is a list but
there is way too much information.

I want something more like:

    > Name of Post (Feb 4, 2017 / making-this-site / programming, web-dev, pelican)

### Laying Out the index.html Template

First we need to add the template into our theme:

    $ touch theme/templates/index.html

We will start by inheriting from `base.html`. This will include the
`header` and `container` we created in the last post.

    {% extends "base.html" %}

Next lets make an unordered list to hold our posts:

    {% block content %}
    <ul>
    {% for article in articles_page.object_list %}
      <li>
        <a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a>
        &nbsp
        <span class="post-meta">({{ article.date.strftime('%b %d, %Y') }}
      {% if article.tags %}
        /
        {% for tag in article.tags %}
          {% if not loop.last %}
           <a href="{{ SITEURL }}/{{ tag.url }}" rel="tag">{{ tag }}</a>,
          {% else %}
            <a href="{{ SITEURL }}/{{ tag.url }}" rel="tag">{{ tag }}</a>)
          {% endif %}
        {% endfor %}
      {% endif %}
      </span>
      </li>
      
    {% endfor %}
    {% endblock content %}


The first thing to notice is the for loop in line 3 itereating over
`articles_page.object_list` this variable provides us with a list of
articles that we can then get information from.

Once we have an article we add `<li>` for it to live and print
out the relevant meta data.

Notice how when adding both the category and tags lists we check first
with an if statement for their existance. This is so we do not get
something like "/ / )" if no categories or tags exist.

### Some CSS Refinement

The freshly added template looks almost exactly how I want it. But
there are two issues from my perspective:

When you are in the mobile view the meta-data for each post looks
awkward:

![Alphabet Soup of Metadata on Mobile](/images/crushed_up_metadata.png)

There is no space between the title and the first article in the
list:

![Tight Spacing Between Title and First Article](/images/tight_title.png)

#### Making Metadata on Mobile Look Good
If you look back up to the code that we added into the template you
will notice that all that all the metadata for a post is contained in
a span with the class of `post-meta`.

Let's define `post-meta` in the "default && mobile" section of
`jaredandrews.css` like so:

	.post-meta {
		display: inline-block;
	}

This change makes entire span jump to the next line when any part of
it can't fit into the parent container:

![Post metadata with display as inline-block](/images/inline_block_metadata.png)

This is better but I don't like how the metadata falls underneath the
bullet point. Instead I would like it to align with the post title. To
achieve this we an the following to the "default && mobile" section of `jaredandrews.css`

	li {
		list-style-position: outside;
		margin-left: 1em;
	}

![Metadata aligned with the post title on mobile](/images/aligned_metadata_mobile.png)

Now that's what I'm talking about!

#### Creating Space Between the Title and the List

Next I want to make a little bit of space between the header and the
list. By default Skeleton assigns a bottom margin of `2.5rem` to most
elements. I am going to give my `header` div the same margin by
adding:

	.header {
		margin-bottom: 2.5rem;
	}

### A Quick Aside on Improving Image Display

While I intended to focus strictly on `index.html` in this post I
noticed how bad the images were looking while proofreading and
wanted to do something about it.

First the images don't respond to the width of the screen at all
meaning they bleed of the page. Second, the images have no border,
which can cause confusion, especially when displaying screenshots of
text from this site.

To add a border and make the images scale I added the following css
to the "default && mobile" section of `jaredandrews.css`:

	img {
		max-width: 100%;
		box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 2px 8px 0 rgba(0, 0, 0, 0.2);
	}

This makes the images stay within the width of the screen and provides
a nice border with a shadow.

### Wrapping Up

We now have a home page for the site and it looks pretty much exactly
how I want it to on both mobile and desktop.

If you click a category you will notice that the same `index.html`
template appears to get used to create category pages. Clicking on a
tag will lead to an empty page. We will have to tackle that in the
future!

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/02).

[Commit]() and [diff]() on GitHub.
 
