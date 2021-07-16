import requests

URL = 'https://polymerdatabase.com/polymers/polyacrylamide.html'
page = requests.get(URL)
print(page)
