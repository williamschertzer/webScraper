import requests
from bs4 import BeautifulSoup
import pprint
import csv
#from Scrape import *


'''Find all of the relevant links from each alphabetical page'''



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
    #link = '\"http://polymerdatabase.com/' + link.replace(' ', '%20') + "\""
    link = 'http://polymerdatabase.com/' + link.replace(' ', '%20')
    newlinklist.append(link)
newlinklist = newlinklist[:len(newlinklist)-2]
'''new link list is a list of links for pages by letter'''
newlinklist = newlinklist[1:7]
groupLinks = []
first = []
second = []
third = []
for link in newlinklist:
    page = requests.get(link)
    pp = pprint.PrettyPrinter(indent = 4)
    soup = BeautifulSoup(page.content, 'html.parser')
    resultsAB = soup.find(id = 'wrapper')
    for resultsAB in soup.find_all('div',class_='container'):
        if resultsAB.table != None:
            html = resultsAB
    if html.table.tr.find_all('td'):
        td = html.table.tr.find_all('td')
    else:
        td = html.table.tr.td
    for want in td:
        groupLinks.append(want)
#print(groupLinks)
for new in groupLinks:
    second.append(new.find_all('a'))
for newer in second:
    for newest in newer:
        third.append(newest.get('href'))
firstHalf = third[0:18]
secondHalf = third[19::]
whole = []
for string in firstHalf:
    link = 'https://polymerdatabase.com/' + string.replace(' ', '%20')
    whole.append(link)
for string in secondHalf:
    link = 'https://polymerdatabase.com/polymer%20index/' + string
    whole.append(link)
whole = whole[:len(whole)-1]
'''whole is the list of strings of all polymer groups'''


'''get all polymers from each polyemr group'''

polymerLinks1 = []
polymerLinks2 = []
liLinks = []
for polymer in whole:
    page = requests.get(polymer)
    pp = pprint.PrettyPrinter(indent = 4)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.body.find('div', {'id': 'page'})
    deeper = results.find_all('ul')
    deepest = deeper[3]
    newli = deepest.find_all('li')
    for what in newli:
        liLinks.append(what.a.get('href'))

''' liLinks contains all of the HREFs of every polymer'''


finalLinks = []
for single in liLinks:
    finalLinks.append('http://www.polymerdatabase.com' + single[2::])
finalLinks = list(dict.fromkeys(finalLinks))

finalLinks = [x for x in finalLinks if x != 'https://polymerdatabase.com/polymers/polyvinylbutyral.html']

#for nice in finalLinks:
#    my_scrape(nice)
#my_scrape(finalLinks[0])
