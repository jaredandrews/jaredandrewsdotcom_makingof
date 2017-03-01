Title: Making This Site, Part 8: Page Template
Date: 2017-02-28 18:15 
Tags: programming, web-dev, pelican, jinja2, css, markdown

There are two types of content in Pelican, [articles and pages](http://docs.getpelican.com/en/stable/content.html#articles-and-pages). So far we have only worked with articles. But now that we are nearing the end of creating this site I need to add an "About" page with a bio, contact information and maybe a few other things. In the future I may use pages to host content that will be updated over time but is better preseneted as a single package. For example I intend to add a travel map and log at some point. This would be more suited as a single page that get's updated frequently than a million very brief blog posts.

### Setting Up

We need to create both a template for pages and a place for them to go in the `content` directory. Lets add the new template, a new content directory and a new page:

    $ touch theme/templates/page.html
    $ mkdir content/pages/
	$ touch content/pages/about.md

### Creating the About Page Markdown

Lets start with `about.md`. This is the post that describes the content and metadata for my about page. Working with it is basically the same as an article.

    Title: About
    Date: 2017-02-28 18:15
    Modified: 2017-02-28 18:15

    CONTENT TODO

Notice there is less metadata than an article. I added a `Modified` key which I will update whenever I change this page.

### Creating the Page Template

Next lets edit `page.html`. This is the template that content in `content/pages/` willl be applied to. It is like a simpler article:

    {% from 'macros.html' import get_page_meta_data_html %}
    {% extends "base.html" %}
    {% block title %}{{ page.title }} — {{ SITENAME }}{% endblock %}
    {% block content %}
      <h2 class="article-title">{{ page.title }}</h2>
    
      <footer class="article-metadata">
        {{ get_page_meta_data_html(page) }}
      </footer>
    
      <div>{{ page.content }}</div>
    {% endblock %}

Notice that the CSS classnames are still prepended with "article-". These names not don't make sense, because they are used with pages as well. I doubt I will ever confuse myself with this inconsistency but since I will be using the exact same styles for both type of content I think it's fair to remove the prefix, thus `.article-title` and `.article-metadata` are now `.title` and `.metadata` respectively.

Every thing is pretty similar to `article.html` minus the navigation. I also changed how the metadta was displayed with a new method in `macros.html`:

    {% macro get_page_meta_data_html(page) %}
      Last Modified: 
      {% if page.modified %}
        {{ page.modified.strftime("%b %d, %Y") }}
      {% elif page.date %}
        {{ page.modified.strftime("%b %d, %Y") }}
      {% endif %}
    {% endmacro %}

This shows the "last modification" date for a page and that's it.

### Updating the Nav Bar

A page in `content/pages` is generated with a slug that looks like `pages/page.html`. Thus my new about page will look like `pages/about.html`. I have a link to the About page both in the Nav Bar and on the front page.

To update the Nav Bar I update `base.html`:

    <nav><a href="{{ SITEURL }}/pages/about.html">about</a> / <a href="{{ SITEURL }}/archives.html">archive</a> / <a href="#">rss</a></nav>

In the last post I added a greetings box to `index.html`. I put a link to the about page in it and at the time thought the link would be `{{ SITEURL }}/about.html`. Turns out my assumption was wrong so I updated that `index.html` to reflect the new link.

### Adding Content to the About Page

Next I added content to `about.md`:

	Title: About
	Date: 2017-02-28 18:15
	Modified: 2017-02-28 18:15
	
	![Portrait of Author](/images/jared_large.png){ class='portrait large' }
	
	**Email Me:** jared (at) jaredandrews (dot) com  
    **Online Profiles:** [HN](https://news.ycombinator.com/user?id=jaredandrews), [reddit](https://www.reddit.com/user/jared_and_fizz/), [Instagram](https://www.instagram.com/jtaaaaaa/), [GitHub](https://github.com/jaredandrews), [LinkedIn](https://www.linkedin.com/in/jaredtandrews), [Spotify](https://open.spotify.com/user/1236628403)

	Greetings! My name is Jared Andrews. I am a freelance software developer. I was raised in Central Massachusetts, went to college at WPI, and lived in Allston, MA for serveral years after. I am currently traveling the United States indefinitely. I work remotely with several clients on Android and Web Development projects. If you are interested in working on a project with me, please check out my [Portfolio]() and/or [LinkedIn](https://www.linkedin.com/in/jaredtandrews) and shoot me an email. I would love to build a great app or website with you!

	During my time in Boston I cofounded Rock and Culture blog, [Spark & Fizz](https://sparkandfizz.com) with some of my friends. If you are interested in DIY music and culture I would ask you to check it out. Along with handling the tech side of things I frequently write, edit videos and conduct interviews for Spark & Fizz.

	The purpose of this website is to host content I created that has nowhere else to live. What that entails will become clear over time :D

    ### Technology Interests
    * Structurally Sound Android Deveopment
    * Android UI and Unit Testing
    * Static Sites (Why is everything on the internet so **slow** in 2017!?)
    * Artifical Intelligence
    * Cellular Automata
    * Generative Art
    * The Post Automation World

    ### Other Interests
    * [Hacking](http://www.catb.org/jargon/html/H/hacker.html)
	* DIY Music, DIY everything really
	* Motorcycle Riding and Maintainance
	* [Stoicism](https://en.wikipedia.org/wiki/Stoicism) and [Absurdism](https://en.wikipedia.org/wiki/Absurdism)
	* Rock Climbing
	* SCUBA Diving
	* Fringe Cultures
	* Photography and Video Editing
	
	*Portrait Graphic by [Alyssa Alarcón](https://alyssalarcondesign.com/), based on a photo by [Townsend Colon](https://twitter.com/townsendcolon?lang=en)*.
	
	*Content on this site is copyright 2015 to infinity unless otherwise stated.*  
	*Any code on this site can be considered [MIT licensed](https://opensource.org/licenses/MIT)*.  
	*Any views expressed on this site are those of the author and do not reflect views held by past or present employers.*

That is a lot of text! Mostly using Markdown that we have already seen. New Markdown that hasn't been used before is `  ` (two spaces at the end of a line) which causes the next line to be on a new line, it basically maps to `<br/>`.

The other thing of note is the class I assign the portrait: `{ class='portrait large' }`. This applies the CSS classes `portrait` and `large`. `jaredandrews.css` has been updated with a large class:


    .large {
        display: block;
        float: none;
    }
    
    ...
    
    /* Larger than tablet */
    @media (min-width: 750px) {
        .large {
			display: inline-block;
    		float: left;
        }
        ...
	}

These classes make the text wrap the portrait on "larger than tablet" screen sizes and go under the portrait for mobile screen sizes.

I wanted to include the "current location" shown on `index.html` as well but it turns out that Pelican variables are not available for pages or articles. For now I will only show it on `index.html` tho I would like to display it on the About page in the future. To do this I would need to make a specific page template for the about page. 

### Wrapping Up

The site is done! Well close... I still need to figure out how to turn on RSS and deploy this bad boy! Then I need to actually write more content :D We are getting close!

To see the complete code for the site at this point checkout COMMIT HASH LINK on GitHub. 

To see what the site looked after these changes were made [click here](). 
