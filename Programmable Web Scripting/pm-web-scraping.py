# Based on what you have leaned in this course, web scrape the API lists on 
# this page, and export your result into a CSV file.

# https://www.programmableweb.com/category/all/apis
# OR
# https://www.programmableweb.com/category/tools/api

# Your Python code should scrape the following details from each table row:
# • API Name
# • API (absolute) URL
# • API Category
# • API Description

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os.path

url = "https://www.programmableweb.com/category/all/apis"
home_url = "https://www.programmableweb.com"
api_dict = {}
api_count = 0


while True:
    response = requests.get(url)
    # print(response)
    data = response.text
    # print(data)
    soup = BeautifulSoup(data,'html.parser')
    # print(soup)


    oddapis = soup.find_all('tr',{'class':'odd'})
    for oddapi in oddapis:
        title = oddapi.find("td",{"class":"views-field-pw-version-title"}).text
        description = oddapi.find("td",{"class":"views-field-field-api-description"}).text
        description = description.replace('\n', ' ')
        category = oddapi.find("td",{"class":"views-field-field-article-primary-category"}).text
        link = home_url + oddapi.find('td', {'class': 'views-field-pw-version-title'}).find_next('a').get('href')
        # print('Job Title:', title, '\nCategory', category, '\nDescription', description, '\nLink', link, '\n---')
        api_count += 1
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


    url_tag = soup.find('a',{'title':'Go to next page'})
    if url_tag.get('href'):
        url= home_url + url_tag.get('href')
        print(url)
    else:
        break




# print(api_dict)
print("Total APIs:", api_count)

api_dict_df = pd.DataFrame.from_dict(api_dict, orient = 'index', columns = ['Title','Category','Description', 'Link'])
 
# print(api_dict_df.head())

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

api_dict_df.to_csv(dir_path + '/api_dict.csv')
