import pytest
import string
import random
import time
from PageObjectModel.LoginPage import Login
from PageObjectModel.AddCustomerPage import  AddCustomer
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_003_Login:
    baseUrl = Readconfig.getApplicationURL()
    Username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************Test_003_Login*******************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.password)
        self.lp.Click_Login()
        self.logger.info("**************Login succesfully*****************")

        self.logger.info("*******************Starting Add Customer Test***************************")

        self.Addcust = AddCustomer(self.driver)
        self.Addcust.clickOnCustomerMenu()
        self.Addcust.clickOnCustomerMenu_item()

        self.Addcust.click_ADDnew()

        self.logger.info("********Providing customer info***************")
        self.email = random_generator() + "@gmail.com"
        self.Addcust.set_email(self.email)
        self.Addcust.set_Password(self.password)
        #self.Addcust.setcustomerRoles("Guests")
        self.Addcust.setManagerofVendor_xpath("Vendor 2")
        self.Addcust.setGender("Female")
        self.Addcust.setFirstName("Lavanya")
        self.Addcust.setlastName("P")
        self.Addcust.setDOB("10/08/1995")  #Format :DD/MM/YYYY
        self.Addcust.setCompanyName("Capgemini")
        self.Addcust.SetAdminContent("This is for testing data...............")
        self.Addcust.clickOnSave()

        self.logger.info("*******Saving customer info*******")
        self.logger.info("*******Add customer validation started*******")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("******Add customer Test Passed******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustoer_scr.png")
            self.logger.info("*************Add customer failed*******************")
            assert False == False
        time.sleep(5)
        self.driver.quit()
        self.logger.info("***********End of Homepage title test****************")

def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))




