from selenium.webdriver.common.by import By
import time


class valid_Login:
    email = "//input[@placeholder='Username']"
    txt_pass = "//input[@placeholder='Password']"
    login = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(5)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")

    def clicklogin1(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()





