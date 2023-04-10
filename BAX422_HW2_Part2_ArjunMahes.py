#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:06:07 2023

@author: arjunvelmurugan
"""

##here we go again, importing thingz, duty free
from bs4 import BeautifulSoup
import requests
import re

## 


def us_news():
    try:
        url = "https://www.usnews.com/"
        headers1 = {
                    'User-Agent': 'Mozilla/5.0',  # This is another valid field
                  }
        page = requests.get(url, headers = headers1)
        ## soup cooking
        soup = BeautifulSoup(page.text, 'lxml')
        ###getting just the top stories
        items = soup.find_all("h3",{"class" : "Heading-sc-1w5xk2o-0 ContentBox__StoryHeading-sc-1egb8dt-3 MRvpF fqJuKa story-headline"})
        print("The Top Stories are:")
        for i in range(1,3):
            print(str(items[i].get_text())) ##NOTE: It's picking the health story as top story too, but if we use the div, the regex is complicated
        story_2=str(items[2])
        
        url2=(re.findall('"https://.+"', str(story_2))) ##finding the url using regex commands
        url2=[x.strip('"') for x in url2][0] ##stripping the list excesses
        print(url2[1])
        story2_page = requests.get(url2,headers = headers1) ##reading the news
        soup2 = BeautifulSoup(story2_page.text, 'lxml') ##making soup of the news
        headline=soup2.find("h1",{"class":"Heading-sc-1w5xk2o-0 iQhOvV"}).text ##jumping for a header like CRon
        content=soup2.find_all("div",{"class":"Raw-slyvem-0 bCYKCn"}) ##content regurgitation, tiktok here i come
        
        print("Headline: ", headline) ##just regular old journalism and facebooking
        for i in range (0,4):
            print(content[i].text)
            print("/n")
    except:
        print("haaaiiyyaaah, you use steel spoon on non-stick pan")
        
########calling main blockz


if __name__ == '__main__':
    us_news() ##main character energy
