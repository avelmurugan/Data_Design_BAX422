#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:13:51 2023

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

def q1():
    try:
        #Login page for planespotters
        url='https://www.planespotters.net/user/login'
        #Setting headers Mozilla/5.0 doesn't work, you have to use thu User-Agent you see on the inspect page, i.e. mimic your actual browser
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 
                           'Request URL': url}
        #"here we go" - fabrizio romano, get request for the site
        r = requests.get(url, headers=HEADERS)
        #begin a session and create our soup
        session_request=requests.session()
        bs = BeautifulSoup(r.text, 'html.parser')
        #a csrf token is a form of encryption that usually comes up when there's a form submission
        csrf_token = bs.find('input', attrs={'name': 'csrf'})['value']
        #store cookies from our first page
        cookies_1=r.cookies.get_dict()
        #set up your credentials here
        credentials = {
            'username' : 'thingsidoforclass',
            'password' : 'thingsido',
            'csrf': csrf_token,
            'redirectid':"",
            "remember":"yes"
        }
        #set up the post request now that we are submitting the credentials
        res = session_request.post(url, headers=HEADERS, data=credentials, cookies=cookies_1)
        #get ccokies from this page
        cookies=res.cookies.get_dict()
        #update original cookies with new cookies
        cookies_1.update(cookies)
        #copy paste the link to the member profile page to open it within this session
        URL2="https://www.planespotters.net/member/profile"
        #use the page1 cookies in this get request
        page2 = session_request.get(URL2, cookies=cookies_1, headers=HEADERS)
        #make a soup object of this page
        doc2 = BeautifulSoup(page2.content, 'lxml')
        #parse to check for name and print it
        if 'Arjun Mahesh' in doc2.text:
            print("Your name is in here")
            print(cookies_1)
            print(doc2.text)
    except:
        print("Error with the connection...")

if __name__ == '__main__':
      q1()
