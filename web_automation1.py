from selenium import webdriver
from selenium.webdriver.common.by import By

class Seleniumdriver():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        if locatorType == 'name':
            return By.NAME
        if locatorType == 'linktext':
            return By.LINK_TEXT
        if locatorType == 'classname':
            return By.CLASS_NAME
        if locatorType == 'xpath':
            return By.XPATH
        if locatorType == 'css':
            return By.CSS_SELECTOR
        else:
            print(locatorType,"does not exist, enter a valid locator type")
        return False
    def getElement(self, locator, locatorType='id'):
        locatorType = locatorType.lower()
        bytype = self.getByType(locatorType)
        element = self.driver.find_element(bytype)
        if element:
            print("element found")
        else:
            print("element not found")


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='D:/sw/chromedriver')
    sele = Seleniumdriver(driver)
    driver.get('http://en.wikipedia.org')
    locator = 'searchInput'
    ele = Seleniumdriver.getElement(locator,locatorType='id')
    print(ele)
