#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 19:07:06 2023

@author: arjunvelmurugan
"""

##import box
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import re
import time

######

def bn():
    try:
        #set url with 40 results
        url="https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=40"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        page=requests.get(url, headers=hdr)
        soup = BeautifulSoup(page.content, 'lxml')
        #doup object storing all url's for books in the B&N Top 40, pg1
        top_url=soup.select('div.product-info-view div.product-shelf-title h3.product-info-title a', href=True)
        print(top_url)
        urls=[str(top_url[i]).split()[2] for i in range(0,len(top_url))]
        urls=[urls[i].replace("href=","") for i in range(0, len(urls))] ##removing href's
        urls=[urls[i].replace('"','') for i in range(0, len(urls))] ##removing quotation marks
        urls=["https://www.barnesandnoble.com"+urls[i] for i in range(0,len(urls))]
        assert len(urls)==40 ##constraining length of urls to 40
        ##start of loop to store each page in a file with an iterative filename
        for i in range(0, len(urls)):
            page=requests.get(urls[i], headers=hdr) ##going through each url
            soup = BeautifulSoup(page.content, 'lxml') ##soup-ing each url
            with open("bn_top100"+"_"+str(i+1)+".html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
                file.write(str(soup)) ##writing as string to a file
            time.sleep(5) ##5secondpause
        ##start of loop to print overview section of each page downloaded
        for i in range(0, 40):
            htmlfile=open("bn_top100"+"_"+str(i+1)+".html", "r").read()
            S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
            text=S.find("div",{"class":'text--medium overview-content p-lg-4 p-sm-0 bookseller-cont'}).text #parsing for the overview section
            text=text.replace("\n", "") ##replacing \n's
            print(str(i+1)+":"+text[:100]) ##Printing n and overview content from the links stored as html files
    except:
        print("Error with the connection...")
        
if __name__ == '__main__':
    bn()