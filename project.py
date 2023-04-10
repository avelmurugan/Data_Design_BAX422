#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:51:54 2023

@author: arjunvelmurugan
"""

##import box
from bs4 import BeautifulSoup
#from urllib.request import Request, urlopen
import requests
#import re
import time

###

def bets():
    url = "https://www.fctables.com/user/login/"
    url2 = "https://www.fctables.com/tipster/my_bets/"
    hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    payload = {
                "login_username" : "avelmurugan", # your username here
                "login_password" : "thingsidoforclass",
                "user_remeber" : "1",
                "login_action" : "1"
                }
    
    r1 = requests.post(url, data = payload, headers = hdr)
    #print(r1.text)
    soup1 = BeautifulSoup(r1.content,'lxml')
    with open("fctables_login_check.html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
        file.write(str(soup1))
    
    ##We checked and the page was good! IT TOOK ME FOREVER!
    
    with requests.session() as s:
        p1 = s.post(url, data = payload)
        soup1 = BeautifulSoup(p1.content,'lxml')
        with open("fctables_login_check1.html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
            file.write(str(soup1))
        #print(p1)
        cookies1 = s.cookies.get_dict()
        r1 = requests.get(url2, cookies = cookies1)
        soup2 = BeautifulSoup(r1.content, 'lxml')
        with open("fctables_bets_page.html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
            file.write(str(soup2))
        find = soup2.find(text='Wolfsburg 0-0 vs Bayern Munich')
        print(find)
        ##We have the match and the bet placed

######

def ip():
    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=amazon+gift+card&_sacat=0&LH_Sold=1&rt=nc&LH_Auction=1" 
    ##url for sold amazon gift cards
    hdr = {'User-Agent': 'Mozilla/5.0'}
    ##headers pretending to be Mozilla
    page1 = requests.get(url, headers=hdr)
    ##saving the contents of the page
    soup = BeautifulSoup(page1.content, 'lxml')
    ##creating a soup object for the webpage
    with open("amazon_gift_card_01"+".htm", "w", encoding = 'utf-8') as file: ##naming file as per convention
            file.write(str(soup)) ##converting soup object to string and writing as an .htm file
   
    top_url=soup.select('div.s-item__info.clearfix a.s-item__link', href=True)
    urls=[str(top_url[i]).split()[5] for i in range(0,len(top_url))]
    urls=[str(urls[i]).split('?')[0] for i in range(0,len(urls))]
    urls=[urls[i].replace("href=","") for i in range(0, len(urls))] ##removing href's
    urls=[urls[i].replace('"','') for i in range(0, len(urls))] ##removing quotation marks
    
    ##for some reason ebay started throwing one junk url in the list of product urls
    ##it was the first url, so I decided to remove urls[0]
    ##there has to be a cleaner way to do it, but do I have the time? maybe towards the end
    for i in range(1, 11):
        page=requests.get(urls[i], headers=hdr) ##going through each url
        soup = BeautifulSoup(page.content, 'lxml') ##soup-ing each url
        with open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "w", encoding = 'utf-8') as file: ##cleaning the url and creating a soup
             file.write(str(soup)) ##writing as string to a file
        time.sleep(10) ##10secondpause
    
    ##initialising empty lists for appending within the loop
    title_card =[] 
    winning_bid =[]
    shipping_cost=[]
    
    for i in range(1, 11):
        try: 
            htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
            print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
            S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
            t1 = S.find("span",{"class":'u-dspn'}).text 
            t2 = S.find("span",{"class":'notranslate vi-VR-cvipPrice'}).text ##getting the selling price for combination #1
            t2 = t2.replace("\t","") ##cleaning selling price to remove \t's
            t2 = t2.replace("\n","") ##cleaning selling price to remove \n's
            t3 = S.find("span",{"class":'notranslate sh-cst'}).text ##getting shipping cost for combination #1
            title_card.append(t1) ##appending to the title card list
            winning_bid.append(t2) ##appending to winning bid list
            shipping_cost.append(t3) ##appending to shipping cost list
            print("The Product be:"+title_card[i-1])
            print("The Cost be:"+winning_bid[i-1])
            print("The shippin' be:"+shipping_cost[i-1])    
        except:
            try:
                htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
                S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
                t1 = S.find("span",{"class":'u-dspn'}).text ##getting just the title card
                t2 = S.find("span",{"class":'notranslate vi-VR-cvipPrice'}).text ##getting the selling price for combination #2
                t2 = t2.replace("\t","") ##cleaning selling price to remove \t's
                t2 = t2.replace("\n","") ##cleaning selling price to remove \n's
                t3 = S.find("span",{"class":'notranslate sh-fr-cst'}).text ##getting shipping cost for combination #2
                title_card.append(t1)#parsing for the overview section
                winning_bid.append(t2)
                shipping_cost.append(t3)
                print("The Product be:"+title_card[i-1])
                print("The Cost be:"+winning_bid[i-1])
                print("The shippin' be:"+shipping_cost[i-1])    
            except:
                htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
                S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
                t1 = S.find("span",{"class":'u-dspn'}).text 
                t2 = S.find("span",{"class":'notranslate',"id":'prcIsum'}).text ##getting the selling price for combination #3
                t2 = t2.replace("\t","")
                t2 = t2.replace("\n","")
                t3 = S.find("span",{"class":'notranslate sh-fr-cst'}).text ##getting shipping cost for combination #3
                title_card.append(t1)#parsing for the overview section
                winning_bid.append(t2)
                shipping_cost.append(t3)
                print("The Product be:"+title_card[i-1])
                print("The Cost be:"+winning_bid[i-1])
                print("The shippin' be:"+shipping_cost[i-1])  

##NEVER UNDERSTOOD OR GOOGLED WHY WE USE MAIN, NOW I KNOW

if __name__ == '__main__':
    print("LEt's solve the eBay problems")
    ip()
    print("Let's solve the FC Tables problems")
    bets()






    ##We notice that 5 files are giving us trouble, what do we do?! PANIC SETS IN
    ##Debugging is kinda painful
    ##There's also an issue with the looping, it's over-writing since we're using append
    ##GAAHHHHHHHHH I HAVE LESS THAN 48 HOURS, WHY, GOD, WHy?
    ##UPDATE : EUREKA, THERE ARE 2 TYPES of SALES on eBay
    ##The seller can let it out for a bid or sell at fixed price
    ##We need to write a if/else situation to account for either
    ##phew, that was a close one
    ##except doesn't seem to parse right 
    ##UPDATE 2: There are more than 2 types of pages
    ##Each HTML page is in a different format of code
    ##For us to be able to scrape on the method that I was using, would require mapping out all possible combinationa
    ##of selectors for sale price and shipping
    ##I have included a hack that only parses the webpage of items bidded on, and not items sold.
    ##This way I zero in on a very specific type of html structure and not have to worry about various combinations
    ##I have left my older code in here where I was able to identify and get results for a set of 10 pages
    ##but, when i ran the code all over again, it showed a multitude of errors
    ##I was running out of time and felt this was a project a little out of scope for this assignment

     
    
    #for i in range(1, 10):
    #    try:
    #        htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
    #        print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
    #        S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
    #        t1 = S.find("span",{"class":'u-dspn'}).text 
    #        t2 = S.find("span",{"class":'notranslate',"id":'prcIsum'}).text
    #        t2 = t2.replace("\t","")
    #        t2 = t2.replace("\n","")
    #        t3 = S.find("span",{"class":'notranslate sh-fr-cst'}).text
    #        title_card.append(t1)#parsing for the overview section
    #        winning_bid.append(t2)
    #        shipping_cost.append(t3)
    #        print("The Product be:"+title_card[i-1])
    #        print("The Cost be:"+winning_bid[i-1])
    #       print("The shippin' be:"+shipping_cost[i-1])
    #    except:
    #        try:
    #            htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
    #            #print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
    #            S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
    #            t1 = S.find("span",{"class":'u-dspn'}).text 
    #            t2 = S.find("span",{"class":'notranslate vi-VR-cvipPrice'}).text
    #            t2 = t2.replace("\t","")
    #            t2 = t2.replace("\n","")
    #            t3 = S.find("span",{"class":'notranslate sh-fr-cst'}).text
    #            title_card.append(t1)#parsing for the overview section
    #            winning_bid.append(t2)
    #            shipping_cost.append(t3)
    #            print("The Product be:"+title_card[i-1])
    #            print("The Cost be:"+winning_bid[i-1])
    #            print("The shippin' be:"+shipping_cost[i-1])
    #        except:
    #            htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
    #            #print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
    #            S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
    #            t1 = S.find("span",{"class":'u-dspn'}).text 
    #            t2 = S.find("span",{"class":'notranslate',"id":'prcIsum'}).text
    #            t2 = t2.replace("\t","")
    #            t2 = t2.replace("\n","")
    #            t3 = S.find("span",{"class":'notranslate sh-cst'}).text
    #            title_card.append(t1)#parsing for the overview section
    #            winning_bid.append(t2)
    #            shipping_cost.append(t3)
    #            print("The Product be:"+title_card[i-1])
    #            print("The Cost be:"+winning_bid[i-1])
    #            print("The shippin' be:"+shipping_cost[i-1])
            
         
            
    

 
       
##NEVER UNDERSTOOD OR GOOGLED WHY WE USE MAIN, NOW I KNOW

#if __name__ == '__main__':
#    ip()

            
 
#        for i in range(1, 10):
#            try:
#                htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
#                print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
#                S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
#                t1 = S.find("span",{"class":'u-dspn'}).text 
#                t2 = S.find("span",{"class":'notranslate',"id":'prcIsum'}).text
#                t2 = t2.replace("\t","")
#                t2 = t2.replace("\n","")
#                t3 = S.find("span",{"class":'notranslate sh-fr-cst'}).text
#                title_card.append(t1)#parsing for the overview section
#                winning_bid.append(t2)
#                shipping_cost.append(t3)
#                print("The Product be:"+title_card[i-1])
#                print("The Cost be:"+winning_bid[i-1])
#                print("The shippin' be:"+shipping_cost[i-1])
#            except:
#                try:
#                    htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
#                    #print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
#                    S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
#                    title_card.append(S.find("span",{"class":'u-dspn'}).text)#parsing for the overview section
#                    winning_bid.append(S.find("span",{"class":'notranslate vi-VR-cvipPrice'}).text)
#                    shipping_cost.append(S.find("span",{"class":'notranslate sh-fr-cst'}).text)
#                    print("The Product be:"+title_card[i-1])
#                    print("The Cost be:"+winning_bid[i-1])
#                    print("The shippin' be:"+shipping_cost[i-1])
#                except:
#                    try:
#                        htmlfile=open("amazon_gift_card_sold"+"_"+str(i+1)+".html", "r").read()
#                        #print("filename_used "+"amazon_gift_card_sold"+"_"+str(i+1)+".html")
#                        S=BeautifulSoup(htmlfile, 'lxml') ##creating a soup in loop
#                        t1 = S.find("span",{"class":'u-dspn'}).text 
#                        t2 = S.find("span",{"class":'notranslate',"id":'prcIsum'}).text
#                        t2 = t2.replace("\t","")
#                        t2 = t2.replace("\n","")
#                        t3 = S.find("span",{"class":'notranslate sh-cst'}).text
#                        title_card.append(t1)#parsing for the overview section
#                        winning_bid.append(t2)
#                        shipping_cost.append(t3)
#                        print("The Product be:"+title_card[i-1])
#                        print("The Cost be:"+winning_bid[i-1])
#                        print("The shippin' be:"+shipping_cost[i-1])
#                    except:
#                        print("This webpage seems not in combinations expected")
 
        
 
    

    