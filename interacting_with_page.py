from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/sw/chromedriver')
driver.get('http://codepad.org')

text_area = driver.find_element_by_id('textarea')
text_area.send_keys('This text is send using Python code.')

text = driver.find_element_by_xpath('//*[@id=editor-form]')