#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:26:49 2023

@author: arjunvelmurugan
"""

##importing thingz
from bs4 import BeautifulSoup
import requests
import re
######## defining function to pull list price, sale price

def kleenex(m1):
    m1 = re.sub(",","",m1) #removing commas, oxford or otherwise
    m1 = re.sub("\$","",m1) # removing dolla sign
    w1 = str(re.findall(r'\d{4}', m1)) #extract what puts a hole in thou pocket
    w2 = str(re.findall(r'[\.\s]\d{2}', m1)) #extract what we feel is inconsequential, but 99c is Rs.80 in India
    w2 = str(re.sub(r'[\s\.]',"",m1)) #removing all that excess
    return w1[2:6] + "." + w2[2:4] #joins joins everywhere, wanted to use just v1 + v2, didnt work, so hacked it to do the job for current assignment


def main():
    try:
        url = "https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"
        headers1 = {
                    'User-Agent': 'Mozilla/5.0',  # This is another valid field
                  }
        page = requests.get(url, headers = headers1)
        ## soup cooking
        soup = BeautifulSoup(page.text, 'lxml')
        ##getting the list price from the website, right click on element and copy the selector
        items1 = soup.select("#ProductReview > div.col-sm-12.col-lg-5.pdp-specs-info > div > div.pdp-price > p.list-price > span:nth-child(3) > del")
        lp = str(items1[0].get_text())
        lp = kleenex(lp) ##cleaning the text we found when we looked up the list price
        ##getting the selling price from the website, right click on element and copy the selector
        items2 = soup.select("#ProductReview > div.col-sm-12.col-lg-5.pdp-specs-info > div > div.pdp-price > p:nth-child(3) > span.sale-price > span.sr-only")
        sp = items2[0].get_text()
        sp = kleenex(sp) ##cleaning the text we found when we looked up the selling price
        print('Selling price and list price are: '+sp+';'+lp) ##fuuiiiyyyyoooohhhh
        
    except: print("Error boys, shut it down!")

########calling main blockz


if __name__ == '__main__':
    main() ##main character energy

#############################################################################



     
     
     
     
     
     
     