import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen() # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("**********SearchCustomerByName_005**********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(5)
        self.logger.info("*********Login Successful*********")

        self.logger.info("*********Starting Search Customer By Name*********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("**********Searching Customer by Name*********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("John")
        searchcust.setLastName("Smith")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("John Smith")
        self.driver.close()
        assert True==status
        self.logger.info("*********TC_SearchCustomerByName_005 Finished*********")

