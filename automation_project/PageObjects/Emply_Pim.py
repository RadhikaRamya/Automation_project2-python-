from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class PIMEmployee:
    addemp_xpath = "button[class='oxd-button oxd-button--medium oxd-button--secondary']"
    emp_image = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input"
    # "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/div/img"
    # "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input"
    first_xpath = "//input[@placeholder='First Name']"
    middle_xpath = "//input[@placeholder='Middle Name']"
    last_xpath = "//input[@placeholder='Last Name']"
    emp_id = "(//input[@class='oxd-input oxd-input--active'])[2]"
    emp_login1 = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span"
    empuser_xpath = "(//input[@class='oxd-input oxd-input--active'])[3]"
    empcnf_xpath = "(//input[@type='password'])[1]"
    empcnfps_xpath = "(//input[@type='password'])[2]"
    save1 = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
    """
    emplist = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a"
    xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[37]/div/div/div[1]/div[" \
            "2]/div/div/button[2]/i "
            
     """

    personalDtls = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a"
    # "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a"

    nicknm = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input"
    otherId = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"
    licns = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
    exp_dt = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[" \
             "2]/div/div/input "

    ssnNumber = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[" \
                "2]/input "
    sinNumber = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[" \
                "2]/input "
    time.sleep(3)
    nationlty = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[" \
                "2]/div/div/div[1] "
    time.sleep(2)
    orignal_natlty = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[" \
                     "1]/div/div[2]/div/div[2]/div[6] "
    # "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]"
    #  "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[" \
    # "1]/div/div[2]/div/div[2]/div[3] "

    martail_status = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[" \
                     "2]/div/div[2]/div/div/div[1] "
    single = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[" \
             "2]/div/div[2]/div[2] "
    # //*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div[1]
    time.sleep(2)
    dateOfBirth = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[" \
                  "2]/div/div/input "
    Gender = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[" \
             "2]/div[2]/div/label/span "
    millatiryService = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[" \
                       "2]/input "
    smoke = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[" \
            "2]/div/label/span/i "
    personalSave = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"

    selectblood = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[" \
                  "2]/div/div[1]/div[1] "
    bloodType = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[" \
                "2]/div/div[2]/div[4] "
    # covid_19 = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[
    # 2]/input"
    saveCustom = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button"
    attachmentButton = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button"
    browse = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/input "
    text = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[2]/div/div/div/div[2]/textarea"
    saveAttachments = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[2]"
    pencil = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[3]/div/div/div/div/div/div[1]/div[" \
             "2]/div/div/button[1] "

    def __init__(self, driver):
        self.driver = driver

    def clickemp(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 "button[class='oxd-button oxd-button--medium oxd-button--secondary']").click()

    def setimage(self, findImage):
        self.driver.find_element(By.XPATH, self.emp_image).send_keys(findImage)

    def setfrstnm(self, firstname):
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(firstname)
        time.sleep(3)

    def setmdnm(self, middlename):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys(middlename)

    def setlnm(self, lastname):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(lastname)

    def setid(self, id1):
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(id1)
        time.sleep(2)

    def clickemplogin(self):
        self.driver.find_element(By.XPATH, self.emp_login1).click()

    def setuser(self, empuser):
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys(
            empuser)

    def setempcnf(self, empcnf):
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(empcnf)

    def setempcnfps(self, empcnfps):
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys(empcnfps)

        time.sleep(3)

    def clicksave1(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(4)

    def clickpersonal(self):
        self.driver.find_element(By.XPATH, self.personalDtls).click()
        time.sleep(3)

    def setnknm(self, ncknm1):
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div["
                                           "1]/div[2]/div/div/div[2]/input").send_keys(ncknm1)

    def NewId(self, setnewId):
        self.driver.find_element(By.XPATH, self.otherId).send_keys(setnewId)

    def newlcns(self, setlcns):
        self.driver.find_element(By.XPATH, self.licns).send_keys(setlcns)

    def newExpDt(self, setExpDt):
        self.driver.find_element(By.XPATH, self.exp_dt).send_keys(setExpDt)
        time.sleep(2)

    def setSSN(self, SSNnumber):
        self.driver.find_element(By.XPATH, self.ssnNumber).send_keys(SSNnumber)

    def setSin(self, SINNumber):
        self.driver.find_element(By.XPATH, self.sinNumber).send_keys(SINNumber)

    def clickntnalty(self):
        self.driver.find_element(By.XPATH, self.nationlty).click()
        time.sleep(2)

    def clickorignal_natlty(self):
        self.driver.find_element(By.XPATH, self.orignal_natlty).click()

    def clickmartial_status(self):
        self.driver.find_element(By.XPATH, self.martail_status).click()

    def clicksingle(self):
        self.driver.find_element(By.XPATH, self.single).click()

    def setdatOfBrth(self, birthdate):
        self.driver.find_element(By.XPATH, self.dateOfBirth).send_keys(birthdate)

    def clickgender(self):
        self.driver.find_element(By.XPATH, self.Gender).click()

    def setServ(self, millitary):
        self.driver.find_element(By.XPATH, self.millatiryService).send_keys(millitary)

    def noSmoke(self):
        self.driver.find_element(By.XPATH, self.smoke).click()

    def clickpersonalsave(self):
        self.driver.find_element(By.XPATH, self.personalSave).click()
        time.sleep(3)

    def clickBlood(self):
        self.driver.find_element(By.XPATH, self.selectblood).click()

    def setType(self):
        self.driver.find_element(By.XPATH, self.bloodType).click()

    def clickCustom(self):
        self.driver.find_element(By.XPATH, self.saveCustom).click()
        time.sleep(2)

    def Setatachments(self):
        self.driver.find_element(By.XPATH, self.attachmentButton).click()
        time.sleep(3)

    def SetFile(self, attachments):
        self.driver.find_element(By.XPATH, self.browse).send_keys(attachments)

    def setText(self, enter):
        self.driver.find_element(By.XPATH, self.text).send_keys(enter)
        time.sleep(2)

    def SaveAtachmens(self):
        self.driver.find_element(By.XPATH, self.saveAttachments).click()

    def editPencil(self):
        self.driver.find_element(By.XPATH, self.pencil).click()

