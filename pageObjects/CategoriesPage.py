import time

class Categories:
    btnAddNew_lnktext = "Add new"
    txtName_id = "Name"
    txtDescription_id = "tinymce"
    frame_id = "Description_ifr"
    txtDisplayOrder_css = '#category-display > div.panel-container > div > div:nth-child(7) > div.col-md-9 > span.k-widget.k-numerictextbox > span > span.k-select > span.k-link.k-link-increase'
    btnSave_name = "save"
    tblrows_css = "tbody>tr"
    lnkCatalog_lnktxt = "Catalog"
    lnkCategories_lnktxt = "Categories"
    numOfPages_css = "#categories-grid_paginate > ul > li"

    def __init__(self, driver):
        self.driver = driver

    def clickAddNew(self):
        self.driver.find_element_by_link_text(self.btnAddNew_lnktext).click()
        self.driver.implicitly_wait(2)

    def setName(self, name):
        self.driver.find_element_by_id(self.txtName_id).send_keys(name)

    def setDescription(self, description):
        self.driver.find_element_by_id(self.txtDescription_id).send_keys(description)

    def setDisplayOrder(self, number):
        for num in range(number):
            self.driver.find_element_by_css_selector(self.txtDisplayOrder_css).click()

    def switchToDescriptionFrame(self):
        iframe =self.driver.find_element_by_id(self.frame_id)
        self.driver.switch_to.frame(iframe)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def clickSave(self):
        self.driver.find_element_by_name(self.btnSave_name).click()
        self.driver.implicitly_wait(2)

    def clickCatalog(self):
        self.driver.find_element_by_link_text(self.lnkCatalog_lnktxt).click()
        self.driver.implicitly_wait(2)

    def clickCategories(self):
        self.driver.find_element_by_link_text(self.lnkCategories_lnktxt).click()
        self.driver.implicitly_wait(2)

    def getRows(self):
        num_of_rows = self.driver.find_elements_by_css_selector(self.tblrows_css)
        return num_of_rows

    def getPages(self):
        num_of_pages = self.driver.find_elements_by_css_selector(self.numOfPages_css)
        return num_of_pages

    def pageClick(self, page_num):
        pageBtn = self.driver.find_element_by_css_selector("[data-dt-idx='" + str(page_num) + "']")
        pageBtn.click()

    def checkList(self, exp_name):
        flag = False
        num_of_pages = self.getPages()
        for page in range(1, len(num_of_pages)-1): # don't include arrow buttons, loops through each page until Name is found in table
            num_of_rows = self.getRows()
            for item in range(1, len(num_of_rows) + 1):
                act_name = self.driver.find_element_by_css_selector("#categories-grid > tbody > tr:nth-child(" + str(item) + ") > td:nth-child(2)").text
                if exp_name == act_name:
                    flag = True
                    break
            self.pageClick(page + 1)
            time.sleep(2)
        return flag

