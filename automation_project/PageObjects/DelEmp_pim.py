from selenium.webdriver.common.by import By
import time


class DltEmply:
    EmplName = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input "
    charlie = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[" \
              "2]/div/span "
    search = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    enterCharlie = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div"
    DelCharlie = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button"
    yesDelete = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def serchname1(self, Name1):
        self.driver.find_element(By.XPATH, self.EmplName).send_keys(Name1)

    def clickcharlie(self):
        self.driver.find_element(By.XPATH, self.charlie).click()

    def searchCharlie(self):
        self.driver.find_element(By.XPATH, self.search).click()

    def setCharlie(self):
        self.driver.find_element(By.XPATH, self.enterCharlie).click()

    def clickDelcharlie(self):
        self.driver.find_element(By.XPATH, self.DelCharlie).click()

    def clickYes(self):
        self.driver.find_element(By.XPATH, self.yesDelete).click()
