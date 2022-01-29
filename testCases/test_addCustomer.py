import string
import random
import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("********************Test_003_AddCustomer*********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(5)
        self.logger.info("*********************Login Succesful*********************")

        self.logger.info("*********************Starting Add Customer Test*********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()
        #self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[1]/div[2]/button/i[1]").click()

        self.logger.info("**************Providing customer info***************")

        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Aditya")
        self.addcust.setLastName("Dhal")
        self.addcust.setDob("12/06/1997") # Fromat: D / MM / YYYY
        self.addcust.setCompanyName("Cyient")
        self.addcust.setAdminContent("Hello World This is the testing.............")
        self.addcust.clickOnSave()

        self.logger.info("********************Saveing Customer Info**********************")

        self.logger.info("********Add customer validation started*********")

        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******Add customer Test Passed******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


