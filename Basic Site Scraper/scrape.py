import csv
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from textstat.textstat import textstat
import json
import os.path
import pathlib
from collections import Counter

def parse_page(url):
    r = requests.get(url, headers=headers)
    html = r.text.strip()
    soup = BeautifulSoup(html, 'lxml')
    
    # Header Content
    header = soup.find(class_='entry-header')
    read_time = extract_read_time(header)
    title = extract_title(header)

    author = extract_author(header)
    categories = extract_categories(header)

    date = extract_date(header)
    dt = parser.parse(date)
    month = dt.strftime("%B")
    weekday = dt.strftime("%A")
    
    # Body Content
    content = soup.find(class_='entry-content')
    word_count = len(content.text.split())
    reading_level = textstat.flesch_kincaid_grade(content.text)

    links = content.find_all("a")
    link_count = len(links)

    images = content.find_all("img")
    image_count = len(images)
    
    page_data = {
        'reading_time' : read_time,
        'title': title,
        'date': date,
        'month': month,
        'weekday': weekday,
        'author': author,
        'categories': categories,
        'word_count': word_count,
        'reading_level': reading_level,
        'link_count': link_count,
        'image_count': image_count,
        'url': url
    }
    
    return page_data
    
def extract_read_time(header):
    html_str = header.find(class_='read-time')
    time_str = html_str.contents[0].strip().lower().split()[0]
    time_int = int(time_str)
    return time_int

def extract_title(header):
    html_str = header.find(class_='post-meta-title')
    title_str = html_str.contents[0].strip()
    return title_str

def extract_date(header):
    html_str = header.find(class_='single-post-date')
    date_str = html_str.contents[0].strip()
    return date_str

def extract_author(header):
    html_str = header.find(class_='author-name')
    author_str = html_str.find('a').contents[0].strip()
    return author_str

def extract_categories(header):
    html_str = header.find(class_='single-post-cat')
    categories = html_str.findAll('a')
    cat_names = []
    for cat_link in categories:
        cat_name = cat_link.contents[0].strip().lower()
        cat_names.append(cat_name)
    return cat_names

def parse_category(url):
    r = requests.get(url, headers=headers)
    html = r.text.strip()
    soup = BeautifulSoup(html, 'lxml')
    
    article_cards = soup.findAll(class_='post-content')

    for article in article_cards:
        title = article.find(class_='post-meta-title')
        link = title.contents[0]['href']
        print('Parsing URL:', link)
        page = parse_page(link)
        articles_store.append(page)
        
    next_link = find_next_link(soup)
    
    if next_link is not None:
        print('Next page:', next_link)
        parse_category(next_link)
        
    return None

def find_next_link(soup_item):
    bottom_nav = soup_item.find(class_='navigation')
    
    if bottom_nav == None:
        return None
    
    links = bottom_nav.findAll('a')
    next_page = links[-1]

    if next_page.contents[0] == 'Next':
        next_link = next_page['href']
        return next_link
    
    return None

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'
}

dir_path = os.path.dirname(os.path.realpath(__file__))

articles_store = []

# url = 'https://blog.frame.io/2018/10/01/womans-experience-cutting-blockbusterrs/'
# wmn_exp = parse_page(url)
# print(wmn_exp)
# def parse_for_categories(url):
#     home_page = requests.get(url, headers=headers)
#     html_home = home_page.text.strip()
#     soup_home = BeautifulSoup(html_home, 'lxml')
#     top_nav = soup_home.find(class_='navbar-collapse')
#     for link in top_nav.find_all("a"):
#         print(link.string)
#     links = top_nav.find_all("a")
#     i = 0
#     while i < len(links):
#         print(links[i]['href'])

#         i += 1
    #print(links)

# bts = 'https://blog.frame.io/category/behind-the-scenes/'
# parse_for_categories(bts)

# parse_category(bts)
# print(len(articles_store))
# print(articles_store[0])

categories = ['post-production', 'color-correction', 'business', 'workflow', 'behind-the-scenes', 'production', 'announcement']

for category in categories:
    url = 'https://blog.frame.io/category/' + category + '/'
    print('Parsing category', category)
    parse_category(url)

print(articles_store[0])

if not os.path.exists(dir_path + '/data/'):
    os.makedirs(dir_path + '/data/')

with open(dir_path + '/data/articles.csv', 'w+', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(articles_store)

with open(dir_path + '/data/articles.json', 'w+') as f:
    json.dump(articles_store, f)

with open(dir_path + '/data/articles.json', 'r') as f:
    articles_store = json.loads(f.read())

times = []
months = []
weekdays = []
authors = []
categories = []
article_length = []

for article in articles_store:
    
    # Average Reading Time
    times.append(article['reading_time'])
    average_time = sum(times) / float(len(times))
    average_time = round(average_time, 2)
    
    # Posts by Month
    months.append(article['month'])
    month_count = Counter(months)
    
    # Posts by Weekday
    weekdays.append(article['weekday'])
    weekday_count = Counter(weekdays)
    
    # Count by Category
    categories += article['categories']
    category_count = Counter(categories)
    
    # Count by Author
    authors.append(article['author'])
    author_count = Counter(authors)

    # Calculate average article length
    article_length.append(article['word_count'])
    average_length = sum(article_length) / float(len(article_length))
    average_length = round(average_length, 2)

print("Total number of article:", len(articles_store))
print("Average reading time:", average_time)
print("Average word length:", average_length)
print("Posts by month", month_count)
print("Posts by weekday", weekday_count)
print("Posts by category", category_count)
print("Posts by author", author_count)

stats = { 
    'reading_time': average_time, 
    'num_articles': len(articles_store),
    'average_length': average_length
}

with open(dir_path + '/data/stats.json', 'w+') as f:
    json.dump(stats, f)

with open(dir_path + '/data/weekday.json', 'w+') as f:
    json.dump(weekday_count, f)
    
with open(dir_path + '/data/month.json', 'w+') as f:
    json.dump(month_count, f)
    
with open(dir_path + '/data/category.json', 'w+') as f:
    json.dump(category_count, f)

with open(dir_path + '/data/author.json', 'w+') as f:
    json.dump(author_count, f)