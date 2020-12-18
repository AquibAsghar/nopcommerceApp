import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.PageProducts import PageProducts

class Test_searchProductsByName_007:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger
    product_name = "Nike"  # Variable for product you want to search

    def testSearchProductsByName(self, setup):
        self.logger.info("************* TC_searchProductsByName_007 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("************* Navigating to Products Page **********")
        self.pp = PageProducts(self.driver)
        self.pp.clickCatalog()
        self.driver.implicitly_wait(2)
        self.pp.clickProducts()
        self.pp.setProductName(self.product_name)
        self.pp.clickSearch()
        self.logger.info("************* Search for product **********")
        flag = self.pp.searchProductByName(self.product_name)
        assert flag
        self.driver.close()
        self.logger.info("************* TC_searchProductsByName_007 Finished **********")