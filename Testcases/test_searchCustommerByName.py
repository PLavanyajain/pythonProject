import time
from PageObjectModel.LoginPage import Login
from PageObjectModel.AddCustomerPage import  AddCustomer
from  PageObjectModel.SearchCustomerPage import SearchCustomer
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseUrl = Readconfig.getApplicationURL()
    Username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_SearchCustomerbyName(self,setup):
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

        self.logger.info("********searching for customer by Name***************")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("John")
        searchcust.setLastName("Smith")
        searchcust.clickSearch()

        status = searchcust.searchCustomerByName("John Smith")
        assert True == status
        self.logger.info("********Tc_ searchCustomerByName_005 passed***************")