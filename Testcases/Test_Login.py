import pytest
from selenium import webdriver
from PageObjectModel.LoginPage import Login
from Utilities.readProperties import Readconfig
from  Utilities.customLogger import LogGen
#from webdriver_manager.chrome import ChromeDriverManager

class Test_001_Login:
    baseUrl = Readconfig.getApplicationURL()
    Username = Readconfig.getUserName()
    password = Readconfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePage(self, setup):
        self.logger.info("************Test_001_Login*************")
        self.logger.info("************verifiying homepage************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        print(act_title)
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("************homepage test passed*************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePage1.png")
            assert False
            self.driver.close()
            self.logger.info("************homepage test failed*************")


    def test_Loginpage(self,setup):
        #self.driver =  webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassword(self.password)
        self.lp.Click_Login()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************test_Loginpage passed*************")

        else:
            #self.driver.save_screenshot(".\\Screenshots\\" + "test_Loginpage.png")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Loginpage1.png")
            assert False
            self.driver.close()
            self.logger.info("************test_Loginpage failed***************")










