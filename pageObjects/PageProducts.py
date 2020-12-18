class PageProducts:
    lnkCatalog_lnktxt = "Catalog"
    lnkProducts_lnktxt = "Products"
    txtProduct_id = "SearchProductName"
    btnSearch_id = "search-products"

    def __init__(self, driver):
        self.driver = driver

    def clickCatalog(self):
        self.driver.find_element_by_link_text(self.lnkCatalog_lnktxt).click()

    def clickProducts(self):
        self.driver.find_element_by_link_text(self.lnkProducts_lnktxt).click()

    def setProductName(self, product_name):
        self.driver.find_element_by_id(self.txtProduct_id).clear()
        self.driver.find_element_by_id(self.txtProduct_id).send_keys(product_name)

    def getNumOfRows(self):
        return len(self.driver.find_elements_by_css_selector('#products-grid > tbody > tr'))

    def getNumOfCols(self):
        return len(self.driver.find_elements_by_css_selector('#products-grid > tbody > tr > td'))

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def searchProductByName(self, product_name):
        flag = False
        for r in range(1, self.getNumOfRows() + 1):
            actual_product_name = self.driver.find_element_by_css_selector("#products-grid > tbody > tr:nth-child(" + str(r) + ") > td:nth-child(3)").text
            if product_name.lower() in actual_product_name.lower():
                flag = True
        return flag
