#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:08:14 2023

@author: arjunvelmurugan
"""


from pymongo import MongoClient
from urllib.parse import quote_plus

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

##initialising your database for NoSQL querying
db = client.samples_pokemon
#Get collection, from the cluster on Atlas
collection=db['samples_pokemon']

#Question 1:To find names and ids of all pokemon's with candy count >=18 (I was born on 06/12 dd//mm)
for i in collection.find({'candy_count':{'$gte':18}}, {'name':1, "_id":1}):
    print(i)
    
#set or statement to find where num=6 or 12, and return same results as previous query
for i in collection.find({"$or": [{"num":"006"},{"num":"012"}]}, {'name':1, "_id":1}):
    #Loop through collection and print out name and id
    print(i)    
    
#now we use the crunchbase db
db = client.crunchbase
#Get collection from the db
collection_cb=db['crunchbase_database']

#Finding entries with "text" in their tag_list description
for i in collection_cb.find({"tag_list" : {"$regex" : ".*text.*"}}, {'name':1, "_id":1}):
    #Print name and id from collection
    print(i)
 
#Finding (names, id, twitter username) entries of companies founded between 2000-2010 or with email ending with @gmail.com
final_query = collection_cb.find({"$or": [{"founded_year": {"$gte": 2000,"$lte": 2010}},{"email_address": {"$regex": r"\A\S+@gmail\.com$"}}]},{"name": 1,"_id": 1,"twitter_username": 1})
#Loop through and print final query
for i in final_query:
    print(i)
