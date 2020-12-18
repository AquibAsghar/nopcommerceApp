import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/Admin")
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_css_selector('input[value = "Log in"]').click()
driver.find_element_by_link_text("Sales").click()
driver.implicitly_wait(2)
driver.find_element_by_link_text("Orders").click()
driver.implicitly_wait(2)
driver.find_element_by_id("BillingEmail").send_keys("victoria_victoria@nopCommerce.com")
driver.find_element_by_id("search-orders").click()

tblrows = len(driver.find_elements_by_css_selector('table[id="orders-grid"]>tbody>tr'))
tblcols = len(driver.find_elements_by_css_selector('table[id="orders-grid"]>tbody>tr>td'))
print(tblrows)
print(tblcols)

flag = False
for r in range(1, tblrows + 1):
    emailid = driver.find_element_by_css_selector(
        "#orders-grid > tbody > tr:nth-child(" + str(r) + ") > td:nth-child(6)").text
    if emailid == "victoria_victoria@nopCommerce.com":
        flag = True
        print( "it's a match")