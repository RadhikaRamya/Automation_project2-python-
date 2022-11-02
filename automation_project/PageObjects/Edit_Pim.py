from selenium.webdriver.common.by import By
import time


class EditEmplyee:
    EmplName = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    Garry = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[" \
            "2]/div/span "
    searchgarry = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    grid = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div"
    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div "

    pencil = "//div/div/button[2]/i[@class='oxd-icon bi-pencil-fill']"
    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[2]"
    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div"
    # "//*[@id='app']/"
    DavidPersonal = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a"
    davidnickname = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[" \
                    "2]/input "
    otherId = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"
    davidLicence = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[" \
                   "2]/input "
    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[" \
    # "2]/input "

    davidExipry = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[" \
                  "2]/div/div/input "
    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[" \
    # "2]/div/div/input "
    davidSSN = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[" \
               "2]/input "
    davidSIN = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[" \
               "2]/input "
    davidmilitiry = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[" \
                    "2]/input "
    david_smoke = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[" \
                  "2]/div/label/span/i "
    saveGarry = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
    GarryBlood = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[" \
                 "2]/div/div[1]/div[1] "
    selectBloodGroup = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[" \
                       "1]/div/div/div/div[2]/div/div[2]/div[3] "
    addAtachments = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button/i"
    GarryBrowse = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[" \
                 "2]/div/div[1] "

    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def serchname(self, Name):
        self.driver.find_element(By.XPATH, self.EmplName).send_keys(Name)

    def clickgarry(self):
        self.driver.find_element(By.XPATH, self.Garry).click()

    def setGarry(self):
        self.driver.find_element(By.XPATH, self.searchgarry).click()

    def clickgrid(self):
        self.driver.find_element(By.XPATH, self.grid).click()
        time.sleep(2)

    def clickpencil(self):
        self.driver.find_element(By.XPATH, self.pencil).click()
        time.sleep(2)

    def clickDavid(self):
        self.driver.find_element(By.XPATH, self.DavidPersonal).click()
        time.sleep(2)

    def setDavidnickname(self, nikname):
        self.driver.find_element(By.XPATH, self.davidnickname).send_keys(nikname)

    def setotherId(self,Id):
        self.driver.find_element(By.XPATH, self.otherId).send_keys(Id)

    def setLicence(self,licence):
        self.driver.find_element(By.XPATH, self.davidLicence).send_keys(licence)

    def setExpiry(self,expiry):
        self.driver.find_element(By.XPATH, self.davidExipry).send_keys(expiry)

    def setSSN(self,SSN):
        self.driver.find_element(By.XPATH, self.davidSSN).send_keys(SSN)

    def setSIN(self, SIN):
        self.driver.find_element(By.XPATH, self.davidSIN).send_keys(SIN)

    def setmillatiry(self, military):
        self.driver.find_element(By.XPATH, self.davidmilitiry).send_keys(military)

    def set_smoke(self):
        self.driver.find_element(By.XPATH, self.david_smoke).click()

    def clicksave_Garry(self):
        self.driver.find_element(By.XPATH, self.saveGarry).click()

    def clickBlood(self):
        self.driver.find_element(By.XPATH, self.GarryBlood).click()

    def clickBloodGroup(self):
        self.driver.find_element(By.XPATH, self.selectBloodGroup).click()

    def clickAttahments(self):
        self.driver.find_element(By.XPATH, self.addAtachments).click()



