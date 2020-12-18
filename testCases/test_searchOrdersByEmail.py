import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.searchOrdersPage import searchOrders
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchOrdersByEmail_006:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_searchOrdersByEmail(self, setup):
        self.logger.info("************* TC_SearchOrdersByEmail_006 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Navigating to Orders Page **********")
        self.so = searchOrders(self.driver)
        self.so.clickSales()
        self.driver.implicitly_wait(2)
        self.so.clickOrders()
        self.driver.implicitly_wait(2)
        self.logger.info("******* Successfully landed on Orders Page **********")

        self.logger.info("******* Searching Orders By Email **********")
        self.so.setEmail("victoria_victoria@nopCommerce.com")
        self.so.clickSearch()
        flag = self.so.searchOrderByEmail("victoria_victoria@nopCommerce.com")
        assert flag
        self.driver.close()
        self.logger.info("************* TC_SearchOrdersByEmail_006 Finished **********")
