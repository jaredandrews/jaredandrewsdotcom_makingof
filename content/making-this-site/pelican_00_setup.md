Title: Making This Site, Part 0: Setup 
Date: 2015-11-01 10:02 
Tags: programming, web-dev, pelican

Welcome to the first installment of "Making This Site". In these
articles, I will describe the **exact** steps I went through to build
this website. At the end of every article is a link to a commit on
GitHub showing all the code that was added.

### Web Design Goals

The purpose of this website is hosting various projects I work on. The
requirements are simple. I would like:


* A blog presentation
* Lightweight and easy to view on computers and phones
* Easy to maintain and add content to
* Cheap to host

With these requirements in mind, I set out to find a suitable static site generator (SSG). After reading about the pros and cons of many different static site generators I decided on [Pelican](http://docs.getpelican.com/en/3.7.1/index.html).

My decision to use Pelican was primarily based on my pre-existing knowledge of Python and the fact that Pelican had almost all the features I thought I would need and not much more.

### Setting Up Pelican

*For reference I am using Pelican 3.7.1 and Python 2.7.11 on Mac OS 10.12.2*

Setting up Pelican is quite simple, I followed the [quickstart- guide](http://docs.getpelican.com/en/3.7.1/quickstart.html) to get get going.

Running `pelican-quickstart` generates a skeleton site with a default theme. By the end of this article I will have a site that could, theoretically, go online.

Here are the options I used to generate my initial site:

    $ pelican-quickstart
    Welcome to pelican-quickstart v3.6.3.
    
    This script will help you create a new Pelican-based website.
    
    Please answer the following questions so this script can generate the files
    needed by Pelican.
    
    
    > Where do you want to create your new web site? [.] .
    > What will be the title of this web site? Jared Andrews
    > Who will be the author of this web site? Jared Andrews
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
    > What is your URL prefix? (see above example; no trailing slash) http://jaredandrews.com
    > Do you want to enable article pagination? (Y/n) n
	> What is your time zone? [Europe/Paris] Boston
    Please enter a valid time zone:
    (check [http://en.wikipedia.org/wiki/List_of_tz_database_time_zones])
    > What is your time zone? [Europe/Paris]        America/New_York
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
    > Do you want to upload your website using FTP? (y/N) N
    > Do you want to upload your website using SSH? (y/N) N
    > Do you want to upload your website using Dropbox? (y/N) N
    > Do you want to upload your website using S3? (y/N) N
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) N
    > Do you want to upload your website using GitHub Pages? (y/N) N
    Done.

To see the skeleton site I run `./develop_server
start`. `develop_server` reloads the site as files are changed
providing a tight feedback loop when making updates.

### Writing My First Article

After seeing the skeleton site I decided to write the article you are
reading right now. Pelican provides the option to write articles in
Markdown and a number of other languages. I decided to use Markdown,
thhe default option. In the root directory for your site you will find
a `content` directory. This directory is where you store your
articles.


To make this article I used the following command:

    $ touch content/pelican_00_setup.md

#### Article Metadata

Once the file was created I opened it and wrote this article. An
article file needs metadata. The metadata for this article looks like:

    Title: Making This Site, Part 0: Setup 
    Date: 2015-11-01 10:02

##### Tags and Categories

Each post can also have a single category and a list of associated tags. Underneath the title and date information in the Markdown for this post I have also included:

    Tags: programming, web-dev, pelican
    Category: making-this-site

Each post can have a single category. I imagine that typically I will only use categories when I want to group specific posts together, for example, I would want a visitor of this site to be able to to view all of the "Making This Site" posts in one place, thus I have created the `making-this-site` category.

Tags are additional metadata that can be used to find related posts. Typically I will provide a very general tag and then a couple more specific ones.

##### Content

After the metadata you start writing the content of the article. You
can view the complete markdown file for this article [here](TODO).

For this article I used a number of Markdown features within the text. `*` creates a bullet point. `#` indicates that the line is a header. I also prefaced lines of code with at least four spaces so they would be shown in a code block.

### Wrapping Up

At this point, with very little effort, I have a working blog with one article on it. Now I want to make it look good. Next, I will develop a custom Pelican theme.

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/00).

[Changes](https://github.com/jaredandrews/jaredandrewsdotcom_makingof/tree/d53538832006e1b9fe3f9e49b688f8039ee8d12f) on GitHub.
