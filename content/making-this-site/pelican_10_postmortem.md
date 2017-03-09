Title: Making This Site, Part 10: Postmortem
Date: 2017-03-02 10:00
Tags: programming, web-dev, pelican

The site is now finished and deployed. I went through it and proofread
everything. Hopetfully these are articles are now readable :D

### Thoughts on Pelican

Building this website was my first time using Pelican and my first
time making a *finished* website with *any* Static Site Generator.

Overall, I have been satisified with Pelican. I find the default
behaviors to be sensible and easy to understand. Once I understood
the basics of Pelican, I was able to extrapolate on that and make
assumptions instead of looking at the docs. Most of the time my
assumptions were correct.

Pelicans open source nature and plugin architecture makes it easy to
modify and figure out what's going wroing. I looked into the Pelican
source code several times while developing this site and it was easy
to understand and well documented.

I started working on this site in later 2015 and resumed work again in
early 2017. When I resumed work on it I upgraded Pelican from `3.6.3`
to `3.7.1`. Doing this update didn't break any code which was a
pleasant surprise.

### Design Over Time

One cool aspect of this site and it's corresponding repository is that
every commit could be theoretically deployed. I have gone back and
added links to a generated version of the site at the end of every
article.

Here is what the evolution of the index page and first article looked
like over time:

![Animation of front page over time](/images/index_over_time.gif)

![Animation of post over time](/images/post_over_time.gif)

### Keeping the Design Simple

I wanted the design of this site to be simple. A secret goal of mine
was having a website that looks good in the Lynx browser. I think this
goal has been met:

![jaredandrews.com rendered in Lynx](/images/lynx_1.png)

I also wanted it to be readable with no CSS at all:

![jaredandrews.com in Firefox with no styles applied](/images/ff_no_style.png)

Hell yea!

### What's Next

The site is finished and now it really **begins**. I will be adding
content and probably making a lot more changes to the ways it laid
out. I'm not sure if I will continue to document those changes but if
I do something particularily interesting, I will be sure to write
about it.
