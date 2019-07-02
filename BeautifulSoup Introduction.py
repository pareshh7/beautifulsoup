from bs4 import BeautifulSoup
import requests

# Specify the url you wish to open.

url = "http://example.com/"

# Getting the webpage and creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

# Extracting all the <a> tags.
tags = soup.find_all('a')

# Extracting URLs from the attribute 'href' in the <a> tags.
for tag in tags:
    print(tag.get('href'))
