import requests
from bs4 import BeautifulSoup
import pprint
import csv
from Scrape import *


'''Find all of the relevant links within a polymer class'''

#def inner_files(URL):
URL = 'https://polymerdatabase.com/polymer%20index/polyacrylamides.html'

page = requests.get(URL)
pp = pprint.PrettyPrinter(indent = 4)
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.body
wrapper = body.div
print(wrapper)
deep = wrapper.find_all('div')[1]







#ABLinks = []
#for td in trAB.find_all('td'):
#    for par in td.find_all('p'):
#        for a in par.find_all('a'):
#            if a.text:
#                want = a['href'].split()
#                txtFormat = 'https://polymerdatabase.com/polymer%20{0}'.format(want[1])
#                ABLinks.append(txtFormat)
#for ABLink in ABLinks:
#    print(ABLink)
