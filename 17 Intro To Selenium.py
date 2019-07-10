from selenium import webdriver      # imports
from time import sleep
from bs4 import BeautifulSoup


#make a webdriver object and specify the path of chrome driver


driver = webdriver.Chrome('/Users/PARESH/Downloads/chromedriver')


#open some page using get method url


driver.get('https://www.facebook.com')


#driver.page_source


soup = BeautifulSoup(driver.page_source,'lxml')


print(soup.prettify())


#close webdriver object


driver.close()

