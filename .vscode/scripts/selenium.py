import selenium
from selenium import webdriver

driver=webdriver.chrome()
driver.get('https://www.reddit.com/')
print('opening browser')