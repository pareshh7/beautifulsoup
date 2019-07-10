from selenium import webdriver #imports
from time import sleep


#make a web driver object and specify the path


driver = webdriver.Chrome('/Users/PARESH/Downloads/chromedriver')


# instagram example


driver.get('https://www.instagram.com')


sleep(2)


#finding button using xpath


login_button = driver.find_element_by_xpath("//span[@id='react-root']//p[@class='_dyp7q']/a") # valid


login_button.click()


sleep(5)


# google example


driver.get('https://www.google.com')


sleep(2)


#finding search bar using xpath


searchbar = driver.find_element_by_xpath("//input[@id='lst-ib']")       #


searchbar.send_keys('valid xpath expression')


searchbar.submit()


sleep(5)


driver.close()
