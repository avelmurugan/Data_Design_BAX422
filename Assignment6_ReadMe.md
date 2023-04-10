#BAX422 - Assignment 6

While many of you have done so already before our last lecture, we want each of you to successfully install MongoDB on your system and get your programming language of choice (Python or Java) to connect to it.  Therefore, please do the following:

Install MongoDB on your system (https://www.mongodb.com/try/download/communityLinks to an external site. “on-premises”). I recommend also installing a GUI so that you can quickly see what's going on (e.g., Studio 3T).
Download the sample MongoDB dumps I uploaded to Canvas (in “Class 7”) (including the Pokémon sample DB)
Connect your programming language of choice (Python, see e.g. https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodbLinks to an external site. or Java, see e.g. https://www.mongodb.com/blog/post/getting-started-with-mongodb-and-java-part-iLinks to an external site.) to MongoDB.
 

Now:

(Let’s get things started …) Please write code (Python or Java) to query and print to screen all Pokémon character “name”s (and “_id” but not the entire document) with candy_count >= month + day of your birthday  (e.g., my birthday is 2/12 and I query candy_count >= 14 as 2+12 = 14).  (25% of points)   (Note:  the MongoDB operator for “>=” is “$gte”)
(Let’s sprinkle in a little or …) Please write code (Python or Java) to query and print to screen all Pokémon character “name”s (and “_id” but not the entire document) with num = month or num = day of your birthday  (e.g., my birthday is 2/12 and I have to query num = 2 or num = 12).  (25% of points)
MongoDB supports RegEx.  The MongoDB operator for RegEx is “$regex”.  For example, to find all Crunchbase documents that have a (company) name that starts with a lower case character, we can search for “db.crunchbase_database.find({"name" : {$regex : "^[a-z].*"}})”

(And some RegEx as well …) Please write code (Python or Java) to query and print to screen all Crunchbase company “name”s (and “_id” but not the entire document) that have “text” in their “tag_list”.  (25% of points)
(This is the final enemy. This question is equivalent of being in the final level of Super Mario facing Bowser)  Please write code (Python or Java) to query and print to screen all Crunchbase company “name”s and “twitter_username” (and “_id” but not the entire document) that (i) were founded between 2000 and 2010 (including 2000 and 2010), or (ii) email address is ending in “@gmail.com”.  (25% of points)
