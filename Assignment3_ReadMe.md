#Assignment 3 - BAX422

In this assignment we go back in time and visit the online store of the most important bookstore in the United States before Amazon came around:  https://www.barnesandnoble.comLinks to an external site.

We will access the Barnes & Noble Top 100: Book Bestsellers and record the old price, new price, and book description for each result.

 

(1) Do the following IN YOUR BROWSER, no programming required.  Please write down your answers in a txt (concisely written answers please).

Use your browsers development tools.  Open the network tab and analyze the network for the following:

 

a) go to https://www.barnesandnoble.comLinks to an external site. and navigate to “Books” > “B&N Top 100”. Have a look at the URL.
b) navigate to page 2 of “B&N Top 100”. Did the URL change?
c) is there a part of your URL that represents the page number? Is there a variable that represents the number of items per page?
d) try to modify these numbers to view the first page with 40 items of “B&N Top 100”.
e) inspecting the HTML source code of (d), how can we access each book in the list of B&N’s top 40? How can we access each book’s product page URL (e.g., https://www.barnesandnoble.com/w/spare-prince-harry-the-duke-of-sussex/1142564630?ean=9780593593806Links to an external site.)?
 

(2) Let's program!

 

a) Use the URL identified above and write code that loads the first page with 40 items per page of “B&N Top 100”.
b) Take your code in (a) and create a list of each book’s product page URL. This list should be of length 40.
c) Write a loop that downloads each product page of the top 40 books in “B&N Top 100”. e., save each of these pages to your computer using a meaningful filename (e.g., "bn_top100_01.htm"). IMPORTANT: Each page request needs to be followed by at least a 5 second pause!  Remember, you want your program to mimic your behavior as a human and help you make good purchasing decisions.
d) Write a separate piece of code that loops through the pages you downloaded in (c), opens and parses them into a Python or Java xxxxsoup-object. Next, access the “Overview” section of the page and print the first 100 characters of the overview text to screen.
 

Please submit two files:  your answers “[yourname]_answers.txt” and your source code “[yourname]_source.[py OR java]” (source code not markup).
