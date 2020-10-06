from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='D:/sw/chromedriver')
driver.get('http://en.wikipedia.org')
time.sleep(2)
print(driver.title)
logo = driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/a')
logo.click()
random_link = driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div/ul/li[5]/a')
random_link.click()
print(driver.title)
time.sleep(3)
second_random_link = driver.find_element(By.LINK_TEXT,'Random article')
second_random_link.click()
print(driver.title)
search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys('selenium software')
time.sleep(5)
driver.quit()
