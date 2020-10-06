import os
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='D:/sw/chromedriver')

driver.get('http://en.wikipedia.org')
driver.get_screenshot_as_file("cap.png")
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))


driver.close()