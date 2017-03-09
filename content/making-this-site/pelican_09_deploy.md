Title: Making This Site, Part 9: Deployment 
Date: 2017-02-28 22:45 
Tags: programming, web-dev, pelican, make, rss, scp

The site is now complete. I am going to enable RSS and deploy it to my
web host with a single command.

### Publishing the Site

I thought there would be some special steps to enable RSS but it turns
out that I set it up in [Part 0](/making-this-site-part-0-setup.html)
when using `pelican-quickstart`. There is a second config file named
`publishconf.py`. This contains everything from `pelicanconf.py` and
the directives for setting up RSS. Here is what `pelican-quickstart`
generated:

    from __future__ import unicode_literals
    
    # This file is only used if you use `make publish` or
    # explicitly specify it as your config file.
    
    import os
    import sys
    sys.path.append(os.curdir)
    from pelicanconf import *
    
    SITEURL = 'http://jaredandrews.com'
    RELATIVE_URLS = False
    
    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
    
    DELETE_OUTPUT_DIRECTORY = True
    
    # Following items are often useful when publishing
    
    #DISQUS_SITENAME = ""
    #GOOGLE_ANALYTICS = ""

I haven't set up Disqus or Google Analytics but I may in the future so
I am leaving the commented out keys.

The "published" version of the site can be generated with`make
publish`. This generates a site structure with an RSS feed and uses
`http://jaredandrews.com` instead of `localhost:8000`. Those are the
only real differences as far as I can tell.

The RSS feed gets put at `feeds/all.atom.xml` so I updated the Nav Bar to reflect that:

    ... <a href="{{ SITEURL }}/feeds/all.atom.xml">rss</a></nav>

### Setting Up Hosting

I have had "jaredandrews.com" registered on
[Namecheap](http://namecheap.com/) for a long time. I could host the
site there but I decided to go with a cheaper and simpler option,
[NearlyFreeSpeech](https://www.nearlyfreespeech.net/). NearlyFreeSpeech
is pay as you go which makes it great for hosting a simple static
site. I only intend to host html, css and javascript on this site so I
don't need anything more than that. Though NearlyFreeSpeech does
provide some additional features.

I will now detail how I setup a new site with NearlyFreeSpeech.

Once you login to NearlyFreeSpeech click on "accounts" and click
"Create a New Site". Here you will need to select the account to
associate with the new site. This is the account that pays for your
hosting. You should be prompted on how to create an account and
deposit money when you create a NearlyFreeSpeech account.

After selecting an account you create a shortname for your new site, I
went with "jta". After that click "create new site". For now the site
can be accessed with the url provided by NearlyFreeSpeech. Later we
will set up DNS on NameCheap so the site can be accessed from
"jaredandrews.com".

After you create a new site you will be provided with an alias and SSH
information.

I want to add my public key to the server so I can log in to it
without entering a password. NearlyFreeSpeech has a space to add
public keys in the profile section of the website. Once you have that
you can access your server with:

	$ ssh jta@ssh.server.nearlyfreespeech.net

### Pushing the Published Site

    $ make clean
    $ make publish
	$ scp -r output/.alias@ssh.server.nearlyfreespeech.net:/home/public/

After doing this I checked out the site on the NearlyFreeSpeech
provided alias. The files made it there but since all the links
reference "jaredandrews.com" it was fairly inoperational. Lets make
"jaredandrews.com" point to NearlyFreeSpeech.


### Setting Up the Domain

On NearlyFreeSpeech go to the sites panel and select the recently
created site. Click "add a new alias" and use your domain. I added
"jaredandrews.com".

Go to the "domains" panel and under the DNS column click "add". After
that click the newly created "manage" button. Here you will see the
Name Servers your site is using.

First let's log into NameCheap. While trying to login to my account I
discovered that NameCheap blocks the VPN service I use. It doesn't
appear to block it directly though, instead it repeatedly says my
login info is wrong. I resetted my password 3 times before turning off
my VPN. So yea... if you are on a Private Internet Access VPN you
might wanna turn it off before going on NameCheap :(

Once you FINALLY get into NameCheap click "manage" next to your
domain. In the "Name Servers" row select "Custom DNS" and put the
NearlyFreeSpeech servers in the appropriate text boxes. Then click the
green checkmark.

It can take up to 48 hours for the Name Server change to propogate. In
my experience it takes a lot less than that.

Once the Name Server change went through I browsed the site and made
sure everything was working. It was!

![The deployed site viewed in FireFox](/images/deployed_site.png)

It took about 1 hour for the site to show up on my internet connection.

### Adding a 404 Page

While checking out my new site, I decided to see what a 404 page
looked like. The default NearlyFreeSpeech 404 page doesn't look that
great, and it's style is inconsistent with the rest of the site. So I
created my own:

    $ touch /content/pages/404.md

I decided to use `cowsay` to display an error message. This is what
`404.md` looks like:

    Title: 404

         ______________________
        < 404 - Page not found >
         ----------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||

Pelican doesn't have anyway to handle error pages, as this is
something typically handled by a server. I never figured out how to
show my own error pages with the Python simple server.

To show your own 404 page on an Apache NearlyFreeSpeech server I
added an `.htaccess` file in the `home/public` directory:

    $ ssh jta@ssh.server.nearlyfreespeech.net
    $ touch .htaccess
	$ echo ErrorDocument 404 /pages/404.html >> .htaccess

### Removing Line Numbers From Code Snippets

I noticed that the code snippet for `publishconf.py` above
and the code snippet for `pelicanconf.py` in
[Part 1](/making-this-site-part-1-base-template.html) have line
numbers while the rest of the code snippets do not. These code
snippets are unique in that they had shebangs at the top. This
apparently triggers line numbers in Pelicans syntax highlighting
system. There appears to be a
[way to turn this off explicitly when using RST as the markdown language](http://docs.getpelican.com/en/stable/content.html?highlight=syntax%20highlighting#syntax-highlighting)
but not when you using Markdown. Thus I have removed the shebang lines
from both places as I don't really find the line numbers useful.

### Wrapping Up

At this point the site is live. I need to go back and do spell
checking and probably clean up a few design related issue. I also need
to go thru each post and include GitHub links.

To view this site the way it looked once all the changes described in this article were made, [click here](/making-this-site-rendered/09).

[Commit]() and [diff]() on GitHub.
