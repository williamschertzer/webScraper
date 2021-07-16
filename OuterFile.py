import requests
from bs4 import BeautifulSoup
import pprint
import csv
from Scrape import *


'''Find all of the relevant links for each class alphabetically'''

URLhome = 'https://polymerdatabase.com/home.html'
page = requests.get(URLhome)
pp = pprint.PrettyPrinter(indent = 4)
soup = BeautifulSoup(page.content, 'html.parser')

headerwrapper = soup.body.div.div
resultsmenu = headerwrapper.find_all('div')
linkbox = resultsmenu[3].find_all('a')
linklist = []
for link in linkbox:
    linklist.append(link.get('href'))

newlinklist = []
for link in linklist:
    link = '\"http://polymerdatabase.com/' + link.replace(' ', '%20') + "\""
    newlinklist.append(link)

newlinklist = list(dict.fromkeys(newlinklist))

'''new link list is a list of links for pages by letter'''
