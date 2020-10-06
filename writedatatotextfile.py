from selenium import webdriver
import os
import io

driver = webdriver.Chrome(executable_path='D:/sw/chromedriver')
driver.get('https://python.org')
html = driver.page_source

with io.FileIO("pagesource.txt", 'w') as file:
    file.write(html.encode("utf-8"))

driver.close()
