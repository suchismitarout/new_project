from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/sw/chromedriver')
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))


driver.close()
