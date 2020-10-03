#Write a Python program to create the combinations of 3 digit combo.
numbers = []
for num in range(100):
    num = str(num).zfill(3)
print(num)
numbers.append(num)

#Write a Python program to count the number of each character of a given text of a text file. 
'''import collections
import pprint
file_input = input('File Name: ')
with open(file_input,'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)'''

#Write a Python program to get the top stories from Google news.
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)



























