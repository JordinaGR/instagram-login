from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

class Main:
    def __init__(self, user, passw, driver):
        self.user = user
        self.passw = passw
        self.driver = driver

    def TancaDriver(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(4)
        usuari_elem = driver.find_element_by_xpath("//input[@name='username']")
        usuari_elem.clear()
        usuari_elem.send_keys(self.user)
        contra_elem = driver.find_element_by_xpath("//input[@name='password']")
        contra_elem.clear()
        contra_elem.send_keys(self.passw)
        contra_elem.send_keys(Keys.RETURN)


user = str(input("username: "))
passw = str(input("password: "))

a = Main(user, passw, webdriver.Chrome())
a.login()
