from selenium import webdriver #imports
from time import sleep


#create web driver object and specify the path


driver = webdriver.Chrome('/Users/waqarjoyia/Downloads/chromedriver')


# open instagram.com -- > url --> https://www.instagram.com


driver.get('https://www.instagram.com')


sleep(5)


#find button using link text


login_button = driver.find_element_by_link_text('Log in')


#clicking the button found


login_button.click()


sleep(5)


driver.close()
