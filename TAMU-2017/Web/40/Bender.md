### Challenge Hint:

My story is a lot like yours, only more interesting ‘cause it involves robots.

[http://web3.ctf.tamu.edu](http://web3.ctf.tamu.edu/)

### Challenge Solution:

The link takes you to a site with a .gif of Bender from Futurama dancing. The hint says that some 'story' is a lot like mine, except it involves ‘robots.’ A quick Google search of some words from the clue will tell you what you need to get started, but this is a very straight forward reference to the standard ‘**robots.txt**’ file websites use to let web-crawlers know what they can’t crawl.

If we use the link proved in the challenge and add ‘**/robots.txt**’ to the end (getting: [http://web3.ctf.tamu.edu/robots.txt](http://web3.ctf.tamu.edu/robots.txt)) we see the following after following the link:

>User-agent: *
>
>Disallow: oiuwerljk.html

The ‘**Disallow:**’ line shows us what web site extension is safe from web crawlers (meaning you will never find this web extension for this site on Google or DuckDuckGo). We can, however, just plug this extension into the base domain and see what happens.

We go to [http://web3.ctf.tamu.edu/oiuwerljk.html](http://web3.ctf.tamu.edu/oiuwerljk.html) and we see the flag:

**gigem{craw1ing_bot$!}**
