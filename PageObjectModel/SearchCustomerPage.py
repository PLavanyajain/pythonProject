class SearchCustomer:
    txt_email_by_id = 'SearchEmail'
    txt_FirstName_id = 'SearchFirstName'
    txt_lastName_id = 'SearchLastName'
    btn_search_by_xpath = "//button[@id='search-customers']"
    tableSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txt_email_by_id).clear()
        self.driver.find_element_by_id(self.txt_email_by_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txt_FirstName_id).clear()
        self.driver.find_element_by_id(self.txt_FirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txt_lastName_id).clear()
        self.driver.find_element_by_id(self.txt_lastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btn_search_by_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def  getNoofColumns(self):
        return len(self.driver.find_elements_by_xpath(self.getNoofColumns))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid ==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
            break
        return flag















