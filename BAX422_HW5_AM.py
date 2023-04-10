#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:16:20 2023

@author: arjunvelmurugan
"""

import warnings
import requests
import json
import codecs
from bs4 import BeautifulSoup
import os
from google.cloud import bigquery

##My device was unable to connect to mysql after hours of effort. I did not have any time to debug
##I chose to use the Google Cloud and BigQuery
##The functionality is almost the same.
##Key differences are that the Query structures differ slightly while using BQ
## Using Google Cloud and setting an external access to DB requires creating a Service Account and key
##My service account key is stored below
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/arjunvelmurugan/Desktop/MSBA/BAX422/singular-apogee-378401-17e34eee848a.json'


def run_query(query):
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()
    return results

def table_creation():
    SQL_DB = "BAX452_HW5"
    SQL_TABLE = "apache_hadoop"
    SQL_TABLE_DEF = "(" + \
                "login STRING(50)" + \
                ",id NUMERIC(25)" + \
                ",location STRING(1000)" + \
                ",email STRING(1000)" + \
                ",hireable STRING(1000)" + \
                ",bio STRING(2000)" + \
                ",twitter_username STRING(1000)" + \
                ",public_repos NUMERIC(25)" + \
                ",public_gists NUMERIC(25)" + \
                ",followers NUMERIC(25)" + \
                ",followings NUMERIC(25)" + \
                ",created_at TIMESTAMP" + \
                ")"
    
    ## Create a BigQuery table with the required columns
    create_db_query = f"CREATE SCHEMA {SQL_DB}"
    print(create_db_query)
    run_query(create_db_query)
    
    create_table_query = f"CREATE TABLE {SQL_DB}.{SQL_TABLE} {SQL_TABLE_DEF}"
    print(create_table_query)
    run_query(create_table_query)
    
    username = 'avelmurugan'
    token = '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'
    
    headers = {'Authorization': 'token ' + token}
    
    
    url = "https://api.github.com/repos/apache/hadoop/contributors"
    response = requests.get(url, headers = headers)
    data = json.loads(response.text)
    
    cont_url = []
    for i in range(0, 30):
        
        cont_url.append(data[i]['url'])
        print(cont_url[i-1])
        
        ## Send a GET request to retrieve the user information
        user_response = requests.get(cont_url[i-1],headers=headers)
        user_data = json.loads(user_response.text)
        
        ## Extract the required fields (login, email, followers, following)
        login = user_data.get("login")
        id = user_data.get("id")
        location = user_data.get("location")
        email = user_data.get("email")
        hireable = user_data.get("hireable")
        #bio = user_data.get("bio")
        twitter_username = user_data.get("twitter_username")
        public_repos = user_data.get("public_repos")
        public_gists = user_data.get("public_gists")
        followers = user_data.get("followers")
        followings = user_data.get("following")
        created_at = user_data.get("created_at")
        
        if email is None:
            email = ''
        if login is None:
            login = ''
        if followers is None:
            followers = 0
        if followings is None:
            followings = 0
        if public_repos is None:
            followings = 0
        if public_gists is None:
            followings = 0
            
        ## Convert created_at to a TIMESTAMP format
        created_at = f"TIMESTAMP('{created_at}')"
            
        ## Construct a SQL query to insert the extracted information into the BigQuery table
        insert_query = f"INSERT INTO {SQL_DB}.{SQL_TABLE} (login, id, location, email, hireable, twitter_username, public_repos, public_gists, followers, followings, created_at) VALUES ('{login}', {id}, '{location}', '{email}', '{hireable}', '{twitter_username}', {public_repos}, {public_gists}, {followers}, {followings}, {created_at})"
        print(insert_query)
        ## Execute the SQL query
        run_query(insert_query)

def whoulookinfor():
    
    SQL_DB = "BAX452_HW5"
    SQL_TABLE = "apache_hadoop"
    LTERM = "Tokyo"
    LOGIN = ""
    HIRE = ""
    search_query = f"SELECT * FROM {SQL_DB}.{SQL_TABLE} WHERE location LIKE '%{LTERM}%' AND login like '%{LOGIN}%' and hireable like '%{HIRE}%'"
    run_query(search_query)
    
if __name__ == "__main__":
    table_creation()
    whoulookinfor()
    

    
