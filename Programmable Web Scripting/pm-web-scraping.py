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

# Set static urls, inititalise dictionary and set counter.
url = "https://www.programmableweb.com/category/all/apis"
home_url = "https://www.programmableweb.com"
api_dict = {}
api_count = 0


# Starting at the above url extract the following:
# • API Name
# • API (absolute) URL
# • API Category
# • API Description
# Then mopve onto the next page if there is one.
while True:
    response = requests.get(url)
    # print(response)
    data = response.text
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup)

    # The required data is split between two classes, odds and evens.
    # Need to go through each class and extract the relevant fields.
    oddapis = soup.find_all('tr', {'class': 'odd'})
    for oddapi in oddapis:
        title = oddapi.find(
            "td", {"class": "views-field-pw-version-title"}).text
        description = oddapi.find(
            "td", {"class": "views-field-field-api-description"}).text
        # Remove the new line charachters.
        description = description.replace('\n', ' ')
        category = oddapi.find(
            "td", {"class": "views-field-field-article-primary-category"}).text
        # The href tag does not have it's own class or id, therefore find the next a tag after the title class.
        link = home_url + \
            oddapi.find(
                'td', {'class': 'views-field-pw-version-title'}).find_next('a').get('href')
        # print('Job Title:', title, '\nCategory', category, '\nDescription', description, '\nLink', link, '\n---')
        api_count += 1
        # Add details to the dictionary.
        api_dict[api_count] = [title, category, description, link]

    evenapis = soup.find_all('tr', {'class': 'even'})
    for evenapi in evenapis:
        title = evenapi.find(
            "td", {"class": "views-field-pw-version-title"}).text
        description = evenapi.find(
            "td", {"class": "views-field-field-api-description"}).text
        description = description.replace('\n', ' ')
        category = evenapi.find(
            "td", {"class": "views-field-field-article-primary-category"}).text
        link = home_url + \
            evenapi.find(
                'td', {'class': 'views-field-pw-version-title'}).find_next('a').get('href')
        # print('Job Title:', title, '\nCategory', category, '\nDescription', description, '\nLink', link, '\n---')
        api_count += 1
        api_dict[api_count] = [title, category, description, link]

    # Find the next page url and set it as the main url which runs the while loop
    url_tag = soup.find('a', {'title': 'Go to next page'})
    if url_tag.get('href'):
        url = home_url + url_tag.get('href')
        print(url)
    # If there is no next page the loop can be broken
    else:
        break


# print(api_dict)
print("Total APIs:", api_count)

# Set the dataframe of the data.
api_dict_df = pd.DataFrame.from_dict(api_dict, orient='index', columns=[
                                     'Title', 'Category', 'Description', 'Link'])
# print(api_dict_df.head())

# Determines the current file path.
dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

# Saves data to a CSV file.
api_dict_df.to_csv(dir_path + '/api_dict.csv')
