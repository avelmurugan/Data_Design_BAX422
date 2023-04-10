#BAX422 - Assignment 5

1. Go to https://api.github.comLinks to an external site. and familiarize yourself with the API.

2. Go to https://api.github.com/repos/apache/hadoop/contributorsLinks to an external site. . This is the Apache Hadoop Github Repo's contributors’ endpoint. Extract the JSON corresponding to the first 100 contributors from this API. (Hint: the API request is a GET request and the variable name that handles the items per page is "per_page").  Write Java or Python code that does all this.

3. For each of the 100 contributors extracted in (2), write code that accesses their user information and extracts "login", "id", "location", "email", "hireable", "bio", "twitter_username", "public_repos", "public_gists", "followers", "following", "created_at" (and print those to screen)

4. Write code that creates an SQL database + table, and stores all the information obtained in (3) in it.  Please be cautious of the data type you choose for each collumn and briefly justify your decisions.  What do you choose as Primary Key and why?

5. Optimize your code in (4) to allow for quick look-ups of "login", "location", and "hireable".  I.e., I would like, for example, to run the command  <<  SELECT * FROM table WHERE location = "Tokyo"  >>  fast.  What choices do you make and why?
