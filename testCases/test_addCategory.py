import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.CategoriesPage import Categories

class Test_addCategory_008:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger
    exp_name = "xyz987"
    description = "this is a test"

    def test_addCategory(self, setup):
        self.logger.info("************* TC_addCategory_008 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("************* Navigating to Catalog Page **********")
        self.cp = Categories(self.driver)
        self.cp.clickCatalog()
        self.logger.info("************* Navigating to Categories Page **********")
        self.cp.clickCategories()
        self.logger.info("************* Adding new category **********")
        self.cp.clickAddNew()
        self.cp.setName(self.exp_name)
        self.cp.switchToDescriptionFrame()
        self.cp.setDescription(self.description)
        self.cp.switchToDefaultContent()
        self.cp.setDisplayOrder(10)   #Set the category's display order. 1 represents the top of the list.
        self.cp.clickSave()
        flag =self.cp.checkList(self.exp_name)
        assert flag
        self.logger.info("************* TC_addCategory_008 Finished **********")



