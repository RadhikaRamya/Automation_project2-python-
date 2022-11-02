from selenium.webdriver.common.by import By
import time


class invalid_Login:
    email1 = "//input[@placeholder='Username']"
    txt_pass1 = "//input[@placeholder='Password']"
    login1 = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName1(self, usr):
        self.driver.find_element(By.XPATH, self.email1).send_keys("Admin")
        time.sleep(5)

    def setPassword1(self, psswrd):
        self.driver.find_element(By.XPATH, self.txt_pass1).send_keys("admin")

    def clicklogin2(self):
        self.driver.find_element(By.XPATH, self.login1).click()
