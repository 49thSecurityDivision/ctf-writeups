### Challenge Description:

I just love reading!

[http://web1.ctf.tamu.edu](http://web1.ctf.tamu.edu/)

### Challenge Solution:

If you view the source one the provided web page, you see some hidden html code that looks pretty crazy. 

This is the first challenge, so it is fairly straight forward. What you are looking for is the only string in this wall of text that matches the flag format of '**gigem{text_here}**.'

You can narrow this down by searching the page for the word '**gigem**,' which returns 75 results, but (more importantly) highlights them all. Scrolling through this, I found the only string that matches the proper format is this:

**gigem{F!nD_a_F!AG!}**

This is the solution.
