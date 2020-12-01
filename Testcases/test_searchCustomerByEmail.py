import time
import pytest
from PageObjectModel.LoginPage import Login
from PageObjectModel.AddCustomerPage import AddCustomer
from  PageObjectModel.SearchCustomerPage import SearchCustomer
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseUrl = Readconfig.getApplicationURL()
    Username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_SearchCustomerbyEmail(self,setup):
        self.logger.info("************Test_004_Login*******************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.password)
        self.lp.Click_Login()
        self.logger.info("**************Login succesfully*****************")

        self.Addcust = AddCustomer(self.driver)
        self.Addcust.clickOnCustomerMenu()
        self.Addcust.clickOnCustomerMenu_item()

        self.logger.info("********searching for customer by emailId***************")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("james_pan@nopCommerce.com")
        searchcust.clickSearch()
        #time.sleep(5)
        status=searchcust.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True==status
        self.logger.info("********Tc_ searchCustomerByemailId_004 passed***************")




        #self.logger.info("********searching for customer by name***************")



