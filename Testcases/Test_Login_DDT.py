import pytest
from selenium import webdriver
from PageObjectModel.LoginPage import Login
from Utilities.readProperties import Readconfig
from  Utilities.customLogger import LogGen
from Utilities import XLUtils
import time
#from webdriver_manager.chrome import ChromeDriverManager

class Test_002_DDT_Login:
    baseUrl = Readconfig.getApplicationURL()
    path=".//Testdata/LoginData.xlsx"
    #Username = R eadconfig.getUserName()
    #password = Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_Loginpage_DDT(self,setup):
        #self.driver =  webdriver.Chrome(ChromeDriverManager().install())
        self.logger.info("************Test_002_DDT_Login************")
        self.logger.info("************test_Loginpage_DDT veriying*************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = Login(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("numbers of rows",self.rows)
        lst_status=[] #empty list

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.Click_Login()
            time.sleep(5)

            act_title=self.driver.title
            print(act_title)
            exp_title="Dashboard / nopCommerce administration"
            print(exp_title)
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*******condition passed*******")
                    print("at=et")
                    self.lp.Click_Logout();
                    lst_status.append("Pass")
                elif self.exp== "Fail":
                    self.logger.info("*******condition failed*******")
                    self.lp.Click_Logout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******condition failed*******")
                    #self.lp.Click_Logout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*******condition passed*******")
                    #self.lp.Click_Logout()
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("******Login DDT test passed********")
            print("Login DDT test passed")
            self.driver.close()
            assert  True
        else:
            self.logger.info("*********Login DDT test failed***************")
            print("Login DDT test failed")
            self.driver.close()
            assert False
        self.logger.info("**********End of Login DDT test****************")


##pytest -v -s --html=Reports\reports1.html Testcases\Test_Login_DDT.py --browser=chrome













