
class searchOrders():
    lnkSales_Menu_lnktxt = "Sales"
    lnkOrders_Menu_lnktxt = "Orders"
    txtEmail_id = "BillingEmail"
    btnSearch_id = "search-orders"
    tblrows_css_selector = 'table[id="orders-grid"]>tbody>tr'
    tblcols_css_selector = 'table[id="orders-grid"]>tbody>tr>td'
    table_css_selector = "#orders-grid > tbody > tr:nth-child(1) > td:nth-child(6)"
    lnkSales_lnktxt = "Sales"
    lnkOrders_lnktxt = "Orders"
    txtLname_id = "BillingLastName"


    def __init__(self, driver):
        self.driver = driver

    def clickSales(self):
        self.driver.find_element_by_link_text(self.lnkSales_lnktxt).click()

    def clickOrders(self):
        self.driver.find_element_by_link_text(self.lnkOrders_lnktxt).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setLastName(self, last_name):
        self.driver.find_element_by_id(self.txtLname_id).clear()
        self.driver.find_element_by_id(self.txtLname_id).send_keys(last_name)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNumOfRows(self):
        return len(self.driver.find_elements_by_css_selector('table[id="orders-grid"]>tbody>tr'))

    def getNumOfCols(self):
        return len(self.driver.find_elements_by_css_selector('table[id="orders-grid"]>tbody>tr>td'))

    def searchOrderByEmail(self, email):
        flag = False
        for r in range(1, self.getNumOfRows() + 1):
            valid_email = self.driver.find_element_by_css_selector(
                "#orders-grid > tbody > tr:nth-child(" + str(r) + ") > td:nth-child(6)").text
            if valid_email == email:
                flag = True
                break
        return flag
