#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:56:54 2023

@author: arjunvelmurugan
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import re
import numpy as np
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pymongo import MongoClient
from urllib.parse import quote_plus
import http.client, urllib.parse

##setting headers and parameters required for GET requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
params = {'search_terms': 'Pizzeria','geo_location_terms': 'San Francisco, CA',}

##multiple authentications are required across functions,this is a separate function that initialises MongoDB
##this code was used for the prev assignment
def mongoauth():
    ##Save your username and password here
    username = "avelmurugan"
    password = ""
    
    #quote plus escapes and url encodes passwords and usernames
    #I ran into an error using it directly in the connection string from mongodb atlas
    username_escaped = quote_plus(username)
    password_escaped = quote_plus(password)
    
    # Construct the connection string with the escaped username and password
    connection_string = f"mongodb+srv://{username_escaped}:{password_escaped}@cluster0.1tl4d1b.mongodb.net/?retryWrites=true&w=majority"
    
    # Connect to MongoDB using the connection string as the parameter inside the MongoClient function
    client = MongoClient(connection_string)
    
    return client

## PART 1
def q1_2():
    browser=webdriver.Chrome('chromedriver')
    ##using selenium to access the bored ape yacht club collection
    browser.get('https://opensea.io/collection/boredapeyachtclub?search[sortAscending]=false&search[stringTraits][0][name]=Fur&search[stringTraits][0][values][0]=Solid%20Gold')
    #now initialising soup objects
    page = browser.current_url
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    #initialising url to capture urls for each of the top 8 gold furred nfts
    url = []
    #loop to find top 8 urls, they had href tags, I added the initial part of every link to the string
    for i in range(0,8):
        #i=1
        top_url=soup.select('#main > div > div > div > div.sc-29427738-0.sc-e1213540-0.hDRGXV.flEkxA > div > div.sc-29427738-0.sc-630fc9ab-0.exZPpc.jSPhMX > div.sc-29427738-0.jFfKPa > div.sc-29427738-0.dVNeWL > div > div:nth-child('+ str(i+1) +') > article > a', href=True)
        #print(top_url)
        href_regex = r'href="([^"]*)"'
        url.append(re.search(href_regex, str(top_url)).group(1))
        url[i]=["https://opensea.io/"+url[i]]
        print(url[i])
    
    ##most of the url's were saved with enclosing brackets, this loop removes them and uses the url to 
    ## write the 8 files
    for i in range(0, len(url)):
        url_loop = str(url[i])
        url_loop=url_loop.replace('[','')
        url_loop=url_loop.replace(']','')
        url_loop=url_loop.replace("'",'')
        url_loop
        browser.get(url_loop) ##going through each url
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, 'lxml') ##soup-ing each url
        with open("bayc_"+str(i+1)+".html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
            file.write(str(soup))

## PART 2
def q3():    
    ##initialising mongo and connecting to instance on Atlas
    client = mongoauth()
    
    ##setting the db and and collection
    db = client["boredapes"]
    ba_col = db["bayc"]
    
    #initialising the empty arrays to append data to
    name=[]
    se=[]
    attribute=[]
    for i in range(0, 8):
        htmlfile=open("bayc_"+str(i+1)+".html", "r").read()
        S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
        #names
        name.append(S.find("h1",{"class":'sc-29427738-0 hKCSVX item--title'}).text) #parsing for the names
        #attributes
        se=S.find_all("div",{"class":'Property--value'}) ##finding the attributes section for each bored ape
        values = [value.text.strip() for value in se] #text.strip() seemed to be a common method of string cleaning
        result = ','.join(values) #joining all attributes together, since the pokemon database also used a similar method
        attribute.append(result) 
        docu = {"name" : f"{name[i]}","attribute" : attribute[i]} ##CHECK, It's still printing the attributes with \ characters all over
        ba_col.insert_one(docu) ##inserting into collection entry by entry within the loop
    
##PART 3
## I used curlconverter.com that helps me convert a curl request into cookies and request parameters
## It saves time over going through html
def q4_5():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    params = {'search_terms': 'Pizzeria','geo_location_terms': 'San Francisco, CA',}
    ##get request to go to search page and use the search terms given in params
    response = requests.get('https://www.yellowpages.com/search', params=params, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')    
    with open("sf_pizzeria_search_page.html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
        file.write(str(soup)) ##writing as string to a file
    time.sleep(5)    
    
    ##saving the search page
    htmlfile=open("sf_pizzeria_search_page.html", "r").read()
    S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
    ##here is where I made a mess, there has to be an easier way of doing it, but I used find_all
    ##multiple times to get specific information
    clickable_area = S.find_all("div",{"class":"srp-listing clickable-area mdm"})
    ##element with all names
    names=S.find_all("a",{"class":'business-name'})
    ##element with all ranks
    ranks=S.find_all("h2",{"class":"n"})
    ##element with all ratings
    ta_ratings = S.find_all("div",{"class":"ratings"})
    #print(ta_ratings)
    #print(clickable_area[1].get("h2"))
    #initialising more empty arrays to append data to for later insert into collection
    shopnames = []
    ratings = []
    ranking = []
    urls_yp = []
    for i in range(1,30):
        print(i)
        shopnames.append(names[i].find("span").text)
        y=ta_ratings[i]
        rating = y.get('data-tripadvisor')
        if rating:
            ratings.append(rating)
        else:
            ratings.append("No Rating")
        ranking.append(ranks[i].text.strip().split('.')[0])
        urls_yp.append("https://yellowpages.com"+ranks[i].find('a')['href'])
        
       
    # Connect to MongoDB using the connection string as the parameter inside the MongoClient function
    client = mongoauth()
    
    db = client["yellowpages"]
    ba_col = db["sf_pizzerias"]
    #using insert_one function to insert one by one the data required
    for i in range(0, 29):
        docu = {"name" : f"{shopnames[i]}","ratings" : ratings[i],"ranking":ranking[i],"url":urls_yp[i]} ##CHECK
        ba_col.insert_one(docu)

def q6_7_8():
    client = mongoauth()
    
    db = client["yellowpages"]
    ba_col = db["sf_pizzerias"]
    
    #finding url from the sf_pizzerias collection 
    y=[]
    for i in ba_col.find({},{'_id':0,'url':1}):
        y.append(i['url'])
    
    #looping through all the urls and writing files, i initially used len(y), but it started writing 50+ files
    for i in range(29): 
        print(i)
        url = y[i]
        print(url)
        response = requests.get(url, headers = headers)
        soup1=BeautifulSoup(response.content,'lxml')
        with open("sf_pizzerias_"+str(i+1)+".html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
            file.write(str(soup1)) ##writing as string to a file
        time.sleep(5)
    
    #looping to collect data from the written files for later insertion into collection
    number=[]
    address=[]
    website =[]
    for i in range(0, 29):
        i=1
        htmlfile=open("sf_pizzerias_"+str(i+1)+".html", "r").read()
        S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
        number.append(S.select('#default-ctas > a.phone.dockable > strong')[0].text) #parsing for the overview section")
        address.append(S.select('#default-ctas > a.directions.small-btn > span')[0].text)
        website.append(S.select('#default-ctas > a.website-link.dockable', href=True))
        
    #initialising a geoloc array that captures the api results for the addresses captured earlier
    geoloc=[]
    for i in range(0, 29):
        conn = http.client.HTTPConnection('api.positionstack.com')

        params = urllib.parse.urlencode({
            'access_key': '8f4a7ea2a209e0678695844fe7dce737',
            'query': str(address[i]),
            'limit': 1,
            })
        
        conn.request('GET', '/v1/forward?{}'.format(params))
        
        res = conn.getresponse()
        data = res.read()
        geoloc.append(data.decode('utf-8'))
        
    #looping thorugh and updating the DB with the new data
    for i in range(0, 29):
        search = {"ranking":(i+1)}
        update = {"$set" : {"number" : number[i],"address" : address[i],"geo_location":geoloc[i]}} ##CHECK
        ba_col.update_one(search, update)
    
    
if __name__ == '__main__':
    q1_2()
    q3()
    q4_5()
    q6_7_8()
    
    
    
    
    
    
    
    















