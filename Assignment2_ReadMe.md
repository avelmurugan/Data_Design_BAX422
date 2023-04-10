#BAX422 Assignment 2

Write / complete the code we walked through in class. I intentially only uploaded the Java code we developped in class to Canvas to leave a tiny bit of work to you. Please use the uploaded MSBA page Python example to get started

 - load https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390 Links to an external site.

use your browser's development tools to find a unique way to access its list price and its current price. What do you choose? Please remember, you can choose multiple selectors to get where you want to be. E.g., you may choose to select "span.class1 p.class2" to select the "p" of class "class2" inside of the "span" of class "class1".
 store the prices to strings.
 use Python's (or Java's) regex (!!) functionality to convert the prices to "1234.56" (no dollar sign, comma, just a "." separator for cents)
 print both, the list price and the current price to screen / terminal Write code that
 loads "https://www.usnews.com/"
 "finds" its current "Top Stories" (do not hard-code it's URL!) (You may use your browser's dev tools to find a functioning way to access all the "Top Stories" and then implement the access to them in your code.)
 read + print the URL of the _second_ current top story to the screen (terminal)
load that page 
read + print the header as well as the first 3 sentences of the main body to the screen
Example: the current _second_ "Top Stories" is "Trump Org Gets Max Fine for Tax Fraud" I want your code to load "https://www.usnews.com/", then read all the "Top Stories" (currently "Biden Invited to Address Congress", "Trump Org Gets Max Fine for Tax Fraud", ...), get the URL that the second top story links to ("https://www.usnews.com/news/national-news/articles/2023-01-13/trump-organization-sentenced-to-pay-1-6-million-for-tax-fraud"; this information is stored in the "href" property of the tag "a", i.e., '<a href="https://...">...</a>', store the link to a string + print it to screen, then load the content of the string and read + print the header as well as the first 3 sentences)
