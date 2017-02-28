Title: Making This Site, Part 7: Design Improvements
Date: 2017-02-28 15:30 
Tags: programming, web-dev, pelican, jinja2, css

While the site looks pretty good at this point there are few changes I would like to make to improve the general readability and flow of information. I would also like to make a few things look slightly better.

### Improving Readability of Code Snippets

A few posts back I added a margin to improve the readability of code snippets in these articles. I found that this wasn't enough tho. Much like `img` I am going to add a `box-shadow` around code snippets to make them stick out a little more and not blend in with the text of a post so much.

In `jaredandrews.css`:

    .highlight {
        padding: .25em 1.5em .25em 1.5em;
        margin-bottom: 2em;
        margin-left: 1em;
        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 2px 8px 0 rgba(0, 0, 0, 0.2);
	}

This adds the same `box-shadow` to a `.highlight` as is used with `img`. I also added a bottom and left margins. I felt the code snippets looked better this way.

### More Margins

While the `h3` and `h4` tags used in the posts help guide the flow of informatin I noticed that when looking at a page it all seemed mixed together. I looked at a lot of other websites and found that adding left margins to body to push it out a little bit really improving readability, especially on mobile. Thus I added:

    p {
        margin-left: 1em;
    }

I previously increased the `margin-left` of `li` as well. I need to increase it again to line up with `p` correctly.

    li {
        list-style-position: outside;
        margin-left: 2em;
    }

This manual management of these values is a good argument for adding something like [SASS](http://sass-lang.com/) to my workflow. I'm pretty sure this is easy to do with Pelican but I haven't gotten to the point where I feel the complexity of my custom css file is great enough to introduce another dependency and step to the bulid process. I may do so in the future though.

I also added a small margin at the bottom of `container`. I found the post navigation at the bottom of the page was a little hard to see when it collided directly with the end of the browser window.

    .container {
        margin-bottom: 2rem;
    }

### Font Changes

Since importing Skeleton into the site it has been using whatever the default font Skeleton provides. I wanted to switch things up and use one font for headers and another font for all other text. A friend recently showed me [fontpair.io](http://fontpair.io) which shows you [Google Fonts](https://fonts.google.com/) that go well together. I spent a while on both websites and eventually setted on using [Poppins](https://fonts.google.com/specimen/Poppins) for headers and [Roboto](https://fonts.google.com/specimen/Roboto) for everything else.

    @import url(http://fonts.googleapis.com/css?family=Poppins);
    @import url(http://fonts.googleapis.com/css?family=Roboto);
    
    body {
        font-family: 'Roboto';
    }
    
    h1, h2, h3, h4 {
        font-family: 'Poppins';
    }

You might notice I don't indicate any fallback fonts, if these fonts don't load I am comfortable falling back to whatever Skeleton provides or really, whatever the viewers browser decides to use. I think this site will work with any font that isn't crazy. 

### Putting a Greeting on the Index Page

The index page of this site is looking a little bland. Looking at a lot of other personal sites for programmers, hackers, artists, etc I see a common pattern of including a small "greetings" box on the home page of a site. I decided to do something similar.

I basically wanted a picture of myself and a brief text greeting next to it. In `index.html` I added a new row and put image and text inside it:

    <div class="row">
		<img class="portrait" src="{{ SITEURL }}/images/jared.png" alt="Portrait of the Author"/>

	    <p>
	        Greetings! My name is Jared Andrews, I am a location
	        independent, freelance software
			developer. This website is a place where I put technology and
			writing projects that don't belong anywhere else. If you are
			interested in learning more about me, check out the
			<a href="{{ SITEURL }}/about.html">About page</a>.
		</p>

	    <p>
			<strong>Current Location: </strong>{{ CURRENT_LOCATION }}

	        <br/>
		    <em>
         	  If you are nearby and want to get together and
			  talk technology, motorcycles, DIY music or really anything, get
			  in touch!
		    </em>
		</p>
    </div>

I reference the About page which has not been added yet. I know that the url will be `{{ SITEURL }}/about.html` so I am hardcoding it here instead of adding it later.

I added a portrait image to `content/images` I think it could be argued that this image belongs in `theme/static` but I couldn't decide one way or another so I added it to `content/images`.

I haven't mentioned it at all in the course of writing these articles but I am currently "location independent" (a slight less snobby term for "digital nomad", maybe it's _snobbier_?) I try to meet new people whereever I go and I wanted to make my rough location known on this site. `CURRENT_LOCATION` is a variable I added to `pelicanconf.py`. It is just a string that I will update when my location changes.

I also added some css:

    .portrait {
        box-shadow: none;
        display: inline-block;
        margin: 1.5rem;
        float: left;
	}

This removes the `box-shadow` added to images on this site and embeds the portrait image into the text.

### Deemphasizing Post Metadata

I found that the post metadata included in article lists was a little "noisy" especially when viewing the site on a mobile screen size. I updated the `post-meta` class to change the font size:

    .post-meta {
        display: inline-block;
        font-size: 1.2rem;
	}

I found this made the metadata a little less obtrusive.

### Wrapping Up

Unless my feelings change this is probably the final state of design for this site. What remains is an About page, figuring out to set up RSS and then **DEPLOYMENT**!

To see the complete code for the site at this point checkout COMMIT HASH LINK on GitHub.

To see what the site looked after these changes were made [click here]().
