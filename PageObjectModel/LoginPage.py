##https://admin-demo.nopcommerce.com/
class Login:
    text_username_Id = "Email"
    text_password_Id = "Password"
    login_button = "//input[@class='button-1 login-button']"
    logout_button_Link = "Logout"

    #def __init__(self, driver):
    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.text_username_Id).clear()
        self.driver.find_element_by_id(self.text_username_Id).send_keys(username)

    def setPassword(self, Password):
        self.driver.find_element_by_id(self.text_password_Id).clear()
        self.driver.find_element_by_id(self.text_password_Id).send_keys(Password)

    def Click_Login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def Click_Logout(self):
        self.driver.find_element_by_link_text(self.logout_button_Link).click()








