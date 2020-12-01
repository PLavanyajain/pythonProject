from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnkCustomer_menu = "//a[@href='#']//span[contains(text(),'Customers')]"
    linkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    Link_AddNew_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_Email_find_element_id = "Email"
    txt_Password_find_element_id = "Password"
    txt_FirstName_ByName = "FirstName"
    txt_LastName_ByName = "LastName"
    rd_Gender_Male_id_xpath = "//input[@id='Gender_Male']"
    rd_Gender_Female_id_xpath = "//input[@id='Gender_Female']"
    DateOFbirth_id_xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_name_xpath= "//input[@name='Company']"
    #IsTaxexempt_xpath = "//input[@class='check-box']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitem_Administrator_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_Registerd_xpath = "//span[contains(text(),'Registered')]"
    lstitem_Guests_xpath = "//span[contains(text(),'Guests')]"
    #Managerofvendor_Xpath = "//select[@class='form-control valid']"
    drp_managerofVendor_xpath = "//select[@id='VendorId']"
    #checkBox_Actve_xpath = "//input[@id='Active']"
    txt_Admincomment_xpath = "//textarea[@name='AdminComment']"
    Button_Save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu).click()

    def clickOnCustomerMenu_item(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menuitem_xpath).click()

    def click_ADDnew(self):
        self.driver.find_element_by_xpath(self.Link_AddNew_xpath).click()

    def set_email(self,emailID):
        self.driver.find_element_by_id(self.txt_Email_find_element_id).send_keys(emailID)

    def set_Password(self,password):
        self.driver.find_element_by_name(self.txt_Password_find_element_id).send_keys(password)

    def setcustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        #time.sleep(5)
        if role == 'Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitem_Registerd_xpath)
        elif role == 'Administrators':
            self.driver.find_element_by_xpath(self.lstitem_Administrator_xpath)
        elif role == 'Guests':
            #here user can be registered (or) guest ,only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']//li//span[contains(text(),'Registered')]").click()
            self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
        elif role == 'Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitem_Registerd_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
        time.sleep(3)
        self.driver.find_elecute_scripts("arugments[0].click();",self.listitem)

    def setManagerofVendor_xpath(self,value):
         drp=Select(self.driver.find_element_by_xpath(self.drp_managerofVendor_xpath))
         drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rd_Gender_Male_id_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rd_Gender_Female_id_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rd_Gender_Male_id_xpath).click()
    def setFirstName(self,firstname):
        self.driver.find_element_by_name(self.txt_FirstName_ByName).send_keys(firstname)

    def setlastName(self,lastname):
        self.driver.find_element_by_name(self.txt_LastName_ByName).send_keys(lastname)

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.DateOFbirth_id_xpath).send_keys(dob)

    def setCompanyName(self,copName):
        self.driver.find_element_by_xpath(self.txt_CompanyName_name_xpath).send_keys(copName)

    def SetAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txt_Admincomment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.Button_Save_xpath)































