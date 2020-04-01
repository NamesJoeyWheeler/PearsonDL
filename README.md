# PearsonDL

A Python script that downloads books  from the Pearson website in image format.

# Disclaimer

Only use this for books you LEGALLY own. We do not condone, promote or tolerate the use of this script for illegal purposes.

# What is needed:

-Python (only 3.6 has been tested, but I assume this works with other versions).

-Windows 10 (unknown if working on other OS).

# How to use:

-Open up the .py file (do not run this with Windows CMD).

-Enter the book ID (instructions for how to get it are lower down this readme). Press enter.

-Enter how many pages the book is. You should be able to find out by going onto the last page of the book on the Pearson site. Press enter.

-It will now download the pages into a folder named after the ID which is in the Pearson Books folder. It will close once completed.



# How to get book ID:

-Login to the Pearson website.

-Open up developer tools and go onto network.

-Open the book on Pearson.

-Now keep an eye out in developer tools for something starting with 'manifest?password'. Copy that link.

The link should look something like this:

https://d38l3k3yaet8r2.cloudfront.net/resources/products/epubs/generated/id/foxit-assets/manifest?password=&isCheckPsd=false&form=true
  
-Now copy the id between '/generated' and '/foxit-assets'. You can now use this ID in PearsonDL!

