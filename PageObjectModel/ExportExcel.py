class ExportFile:
    Export_xpath = "//button[@data-toggle='dropdown']"
    ExportToExcel_xpath = "//button[@name='exportexcel-all']"


    def __init__(self,driver):
        self.driver=driver

    def excelPathDownload(self):
        self.driver.find_element_by_xpath(self.Export_xpath).click()

    def exportExcel(self):
        self.driver.find_element_by_xpath(self.ExportToExcel_xpath).click()



