#BAX422 - Assignment 4

Part I

Preparation:

Read and understand the FlightAware code we developed in class.  If you haven’t paid full attention in DDR class 4 (very unlikely), the last 45 minutes of may be very interesting to review;  it will make part 1 a breeze.

Use your browser to create a login on Planespotters.net .  Please choose a username and password that you are willing to share with us as we ask you to share your code.

Verify that your login works:  start an incognito session, navigating to https://www.planespotters.net/user/loginLinks to an external site. , log in, go to your profile page https://www.planespotters.net/member/profileLinks to an external site..

 

Task:

Write code in Java or Python (full source code not markup) that logs into Planespotters.net and verifies that it is logged in my navigating to https://www.planespotters.net/member/profileLinks to an external site. and checking that your username is displayed on the page.  (The task at hand requires at least 2 page-requests.  I have solved it with 3 page-requests but have not tried if less page requests work as well.)  Specifically, your code should do the following:

Access https://www.planespotters.net/user/loginLinks to an external site. using a standard GET request. Read and store the cookies received in the response.  In addition, parse the response and read (and store to a string variable) the value of the hidden input field that will (most likely) be required in the login process.
Make a post request using the cookies from (1) as well as all required name-value-pairs (including your username and passwords).
Get the cookies from the response of the post request and add them to your cookies from (1).
Verifies that you are logged in by accessing the profile page https://www.planespotters.net/member/profileLinks to an external site. with the saved cookies.
Then, print out the following at the end:
The entire Jsoup/BeautifulSoup document of your profile page.
All (combined) cookies from (3).
A boolean value to show your username is contained in the document in part (5)(a).
 

Tips:

Please don’t forget to set the full user agent (e.g., “Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56”) in all of your requests.
Please make sure that you don’t forget to set all hidden input-tag values when trying to log in (there might be one called “csrf” that may be important to set).
 

Please submit two files:  your source code “part1_source.[py OR java]” (source code not markup) as well as a copy of your screen print “part1_screen.txt”.

 

 

Part II

please get Selenium to work on your system. e., try to code something up in Java or Python that starts a browser of your choice, navigates to google.com, and searches for "askew" as well as "google in 1998" (separate searches!)
write a script that goes to bestbuy.com, clicks on Deal of the Day, reads how much time is left for the Deal of the Day and prints the remaining time to screen (console), clicks on the Deal of the Day (the actual product), clicks on its reviews, and saves the resulting HTML to your local hard drive as "bestbuy_deal_of_the_day.htm"
 

Please ensure that there are proper delays after each website interaction.

 

For part 2.1:  please submit 2 screenshots (JPGs)  and the source code

For part 2.2: Source code and console output
