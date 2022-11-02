import time
from _datetime import datetime

from PageObjects.valid_login import valid_Login
from Utilities.readProperties import ReadConfig1
from PageObjects.Emply_Pim import PIMEmployee
from Utilities import employlogger
from PageObjects.Edit_Pim import EditEmplyee


# from Utilities.logger import LogGen

class Test_2:
    baseURl = ReadConfig1.getApplicationURL()
    username = ReadConfig1.getusername()
    password = ReadConfig1.password()
    logger = employlogger.test_logdemo()

    def test_PIM_02(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl)
        vld = valid_Login(self.driver)
        vld.setUserName(self.username)
        vld.setPassword(self.password)
        time.sleep(10)
        vld.clicklogin1()
        time.sleep(5)
        ademp = PIMEmployee(self.driver)
        ademp.clickemp()
        self.logger.info("######### NewEmployee #######")
        self.logger.info("Add employ in the PIM")
        ademp.setimage("C:\\Users\\Harsha\\Downloads\\hd-wallpaper-g45591c345_640.jpg")
        ademp.setfrstnm("Veenam")
        ademp.setmdnm("Radhika")
        ademp.setlnm("Ramya")
        ademp.setid("335")
        ademp.clickemplogin()
        time.sleep(3)
        ademp.setuser("@Radhika")
        ademp.setempcnf("@Radhika123")
        ademp.setempcnfps("@Radhika123")
        time.sleep(3)
        ademp.clicksave1()

        time.sleep(3)
        ademp.clickpersonal()
        time.sleep(2)
        ademp.setnknm("Pandu")
        ademp.NewId("44523")
        time.sleep(3)
        ademp.newlcns("1007")
        ademp.newExpDt("2023-05-22")
        ademp.setSSN("143")
        time.sleep(2)
        ademp.setSin("456")
        time.sleep(2)
        ademp.clickntnalty()
        time.sleep(3)
        ademp.clickorignal_natlty()
        time.sleep(2)
        ademp.clickmartial_status()
        time.sleep(2)
        ademp.clicksingle()
        ademp.setdatOfBrth("1990-05-07")
        ademp.clickgender()
        ademp.setServ("No")
        ademp.noSmoke()
        ademp.clickpersonalsave()
        time.sleep(2)
        ademp.clickBlood()
        ademp.setType()
        # ademp.setCovid_19("1236878")
        ademp.clickCustom()
        time.sleep(3)
        ademp.Setatachments()
        ademp.SetFile("C:\\Users\\Harsha\\Downloads\\hd-wallpaper-g45591c345_640.jpg")
        time.sleep(2)
        ademp.setText("I Completed Projects 1 and 2")
        time.sleep(3)
        ademp.SaveAtachmens()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "save Ramya":
            print("url is correct")
        else:
            time.sleep(3)
            self.driver.save_screenshot("C:\\Users\\Harsha\\Desktop\\automation_project\\Screenshots" + "RamyaPage.png")
            print("Title is wrong")



        



