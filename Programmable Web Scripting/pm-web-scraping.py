# https://www.programmableweb.com/category/all/apis

# Scrape the following details from each table row:
# • API Name
# • API (absolute) URL
# • API Category
# • API Description

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os.path
import urllib.parse as urlparse
from urllib.parse import parse_qs
import datetime
import time

# Set static urls, inititalise dictionary and set counter.
url = "https://www.programmableweb.com/category/all/apis"
home_url = "https://www.programmableweb.com"
page_root = "https://www.programmableweb.com/category/all/apis?page="
api_dict = {}
api_count = 0
break_count = 30
error_count = 0
error_count_max = 20
max_retry_count = 5
retry_count = 1
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36','referrer': 'https://google.com'}
sleep_time = 5
error_sleep_time = 20


# Determines the current file path.
dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
if not os.path.exists(dir_path + '/data/'):
    os.makedirs(dir_path + '/data/')

# Starting at the above url extract the following:
# • API Name
# • API (absolute) URL
# • API Category
# • API Description
# Then mopve onto the next page if there is one.

while True:

    try:
        time.sleep(sleep_time)
        response = requests.get(url, headers=headers)
        # print(response)
        data = response.text
        # print(data)
        soup = BeautifulSoup(data,'html.parser')
        # print(soup)

        # The required data is split between two classes, odds and evens.
        # Need to go through each class and extract the relevant fields.
        oddapis = soup.find_all('tr',{'class':'odd'})
        for oddapi in oddapis:
            title = oddapi.find("td",{"class":"views-field-pw-version-title"}).text
            description = oddapi.find("td",{"class":"views-field-field-api-description"}).text
            # Remove the new line charachters.
            description = description.replace('\n', ' ')
            category = oddapi.find("td",{"class":"views-field-field-article-primary-category"}).text
            # The href tag does not have it's own class or id, therefore find the next a tag after the title class.
            link = home_url + oddapi.find('td', {'class': 'views-field-pw-version-title'}).find_next('a').get('href')
            # print('Job Title:', title, '\nCategory', category, '\nDescription', description, '\nLink', link, '\n---')
            api_count += 1
            # Add details to the dictionary.
            api_dict[api_count] = [title, category, description, link]
            
        evenapis = soup.find_all('tr',{'class':'even'})
        for evenapi in evenapis:
            title = evenapi.find("td",{"class":"views-field-pw-version-title"}).text
            description = evenapi.find("td",{"class":"views-field-field-api-description"}).text
            description = description.replace('\n', ' ')
            category = evenapi.find("td",{"class":"views-field-field-article-primary-category"}).text
            link = home_url + evenapi.find('td', {'class': 'views-field-pw-version-title'}).find_next('a').get('href')
            # print('Job Title:', title, '\nCategory', category, '\nDescription', description, '\nLink', link, '\n---')
            api_count += 1
            api_dict[api_count] = [title, category, description, link]

        
        # Find the next page url and set it as the main url which runs the while loop
        url_tag = soup.find('a',{'title':'Go to next page'})
        if url_tag.get('href'):
            url = home_url + url_tag.get('href')
            print(url)

            #Reset the retry count to zero as now moving on to the next page
            retry_count = 1
     
        else:
            # If there is no next page the loop can be broken
            break

        ###########################################################
        # Added break count to pause the scraping for testing.
        # Uncomment when needed and comment out when not needed.
        # if api_count >= break_count:
        #     break
        ###########################################################

    except Exception as e:
        # The error will be due to the current page having issues.
        # Add the error to the error log.
        f=open(dir_path + "/data/errors.txt", "a+")
        f.write("Error on url " + url + "\tAttempt number " + str(retry_count) + "\t" + str(datetime.datetime.now()) + "\n" + e + "\n")
        

        # Check how many times this page has been attempted.
        # If it has been attempted more than the maximum count change the url to the next page.
        if retry_count <= max_retry_count:
            retry_count += 1
            time.sleep(error_sleep_time)
        else:
            # Move on to the next page and increae the error count, 
            # reset the retry count and add to error log.
            url = page_root + str(int(url.replace(page_root, "")) + 1)
            error_count += 1
            retry_count = 1
            f.write(str(max_retry_count) + "attempts made, moving to next url\t" + str(datetime.datetime.now()) + "\n")
            time.sleep(error_sleep_time)

        f.close()

        # If error count goes over the maximum break the loop.
        if error_count >= error_count_max:
            break
    else:
        continue


# print(api_dict)
print("Total APIs:", api_count)

# Set the dataframe of the data.
api_dict_df = pd.DataFrame.from_dict(api_dict, orient = 'index', columns = ['Title','Category','Description', 'Link'])
# print(api_dict_df.head())

# Saves data to a CSV file.
api_dict_df.to_csv(dir_path + '/data/api_dict.csv')
