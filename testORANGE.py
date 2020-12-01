from selenium import webdriver
#from webdriver_manager.Chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import pytest
class Orangehrm():
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        yield
        self.driver.close()

    def home_page(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == 'OrangeHRM'

    def Login_page(self, setup):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == 'OrangeHRM'


