import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent #import required libraries



ua = UserAgent()


header = {'user-agent':ua.chrome}  #specifying the header


google_page = requests.get('https://www.google.com',headers=header)


soup = BeautifulSoup(google_page.content,'lxml') # html.parser


print(soup.prettify())
