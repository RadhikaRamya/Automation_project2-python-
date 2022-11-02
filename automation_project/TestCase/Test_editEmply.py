import time

from PageObjects.valid_login import valid_Login
from Utilities.readProperties import ReadConfig1
from PageObjects.Edit_Pim import EditEmplyee
from PageObjects.DelEmp_pim import DltEmply
from Utilities import employlogger


class Test_3:
    baseURl = ReadConfig1.getApplicationURL()
    username = ReadConfig1.getusername()
    password = ReadConfig1.password()
    logger = employlogger.test_logdemo()

    def test_PIM_03(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl)
        vld = valid_Login(self.driver)
        vld.setUserName(self.username)
        vld.setPassword(self.password)
        time.sleep(3)
        vld.clicklogin1()
        time.sleep(2)
        ediEmp = EditEmplyee(self.driver)
        self.logger.info("*******Edit Existing Employee ******")
        self.logger.info("Edit Garry Information In PIM")
        time.sleep(2)
        ediEmp.serchname("Garry")
        ediEmp.clickgarry()
        time.sleep(2)
        ediEmp.setGarry()
        time.sleep(4)
        ediEmp.clickgrid()
        time.sleep(3)
        ediEmp.clickpencil()
        time.sleep(3)
        ediEmp.clickDavid()
        time.sleep(2)
        ediEmp.setDavidnickname("morry")
        ediEmp.setotherId("1234")
        ediEmp.setLicence("1995")
        ediEmp.setExpiry("2024-05-10")
        ediEmp.setSSN("578")
        ediEmp.setSIN("789")
        ediEmp.setmillatiry("yes")
        ediEmp.set_smoke()
        ediEmp.clicksave_Garry()
        ediEmp.clickBlood()
        ediEmp.clickBloodGroup()
        act_title = self.driver.title
        if act_title == "editEmployee":
            print("yes")
        else:
            self.driver.save_screenshot("C:\\Users\\Harsha\\Desktop\\automation_project\\Screenshots"+"EditGarry.png")
            print("No")

    def test_PIM_04(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl)
        vld = valid_Login(self.driver)
        vld.setUserName(self.username)
        vld.setPassword(self.password)
        time.sleep(3)
        vld.clicklogin1()
        time.sleep(2)
        delEmp = DltEmply(self.driver)
        self.logger.info("%%%%% Delete Existing Employee %%%%%")
        self.logger.info("&&&& Delete Charlie In PIM")
        time.sleep(2)
        delEmp.serchname1("Charlie")
        delEmp.clickcharlie()
        delEmp.searchCharlie()
        delEmp.setCharlie()
        delEmp.clickDelcharlie()
        delEmp.clickYes()
