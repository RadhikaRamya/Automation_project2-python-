import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from PageObjects.valid_login import valid_Login
from PageObjects.invalid_login import invalid_Login
from Utilities.readProperties import ReadConfig1


class Test_login_1:
    baseURl = ReadConfig1.getApplicationURL()
    username = ReadConfig1.getusername()
    password = ReadConfig1.password()
    baseURl1 = ReadConfig1.getApplicationURL1()
    usr = ReadConfig1.getusername1()
    psswrd = ReadConfig1.password1()

    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl)
        vld = valid_Login(self.driver)
        vld.setUserName(self.username)
        vld.setPassword(self.password)
        time.sleep(10)
        vld.clicklogin1()

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl1)
        notvald = invalid_Login(self.driver)
        notvald.setUserName1(self.usr)
        notvald.setPassword1(self.psswrd)
        time.sleep(10)
        notvald.clicklogin2()
        act_title = self.driver.title
        if act_title == "TomatoHRM":
            print("Title is correct")
        else:
            self.driver.save_screenshot("C:\\Users\\Harsha\\Desktop\\automation_project\\Screenshots"+"HomePage.png")
            print("Title is wrong")



