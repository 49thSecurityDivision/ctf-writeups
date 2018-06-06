### Challenge Description:

We found a suspicious file being downloaded by one of our employees.  
Make sure everything checks out.

### Challenge Solution:

There is a file to download (**breadSticks.bin**). If we download this file and unzip it, we see a small directory of files. Feel free to look around -- there isn’t very much to see -- but I will just skip to the solution. In the breadSticks > word > media folder is a .jpg called image1. You can see this is a picture of breadsticks which is a pretty good sign.

Investigating the image itself returns nothing, but opening the picture in your favorite plain text editor shows that the first line of the text version of the image is the following:

**Flag=justALittleButter**

Entering **justALittleButter** solves the challenge.
