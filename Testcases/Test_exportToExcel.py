import time
import pytest
from PageObjectModel.LoginPage import Login
from PageObjectModel.AddCustomerPage import  AddCustomer
from  PageObjectModel.SearchCustomerPage import SearchCustomer
from PageObjectModel.ExportExcel import ExportFile
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_ExportExcel_006:
    baseUrl = Readconfig.getApplicationURL()
    Username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_ExportExcel(self,setup):
        self.logger.info("************Test_006_Login*******************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.password)
        self.lp.Click_Login()
        self.logger.info("**************Login succesfully*****************")

        self.Addcust = AddCustomer(self.driver)
        self.Addcust.clickOnCustomerMenu()
        self.Addcust.clickOnCustomerMenu_item()

        self.logger.info("**************Test_Export the file to excel*****************")
        self.excelEx=ExportFile(self.driver)
        self.excelEx.excelPathDownload()
        self.excelEx.exportExcel()


