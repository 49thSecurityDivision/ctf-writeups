### Challenge Description:

So many choices...

[http://web2.ctf.tamu.edu](http://web2.ctf.tamu.edu/)

### Challenge Solution:

Going to the link provided takes you to a page with a picture of Cookie Monster and two buttons -- one that says "Veggies" and one that says "Cookies."

After inevitably spending some time reviewing the source code of all of these pages (the one from the description and the ones linked to by the buttons), I realized the image of cookie monster was probably a clue...

If you check your cookies after visiting both pages, you'll notice the cookies from those pages have content that appear to be base64 strings. From the veggie page, the cookie content when converted from base64 reads: '{NO_VEGGIES}.' The content from the cookies page when converted from base64 reads:

**gigem{CrAzzYY_4_CO0k!es}**

This is our solution.
