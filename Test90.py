# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test90(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_90(self):
        driver = self.driver
        driver.get("http://localhost/dashboard/icehrm/app/login.php?logout=1")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Remember me'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Employees'])[1]/i[1]").click()
        driver.find_element_by_id("tabEmployeeEducation").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add New'])[2]/i[1]").click()
        select1 = Select(driver.find_element_by_id('employee'))
        select1.select_by_visible_text('IceHrm Employee')
        select2 = Select(driver.find_element_by_id('education_id'))
        select2.select_by_visible_text('Bachelors Degree') 
        driver.find_element_by_xpath("//*[@id='institute']").send_keys("NITK")
        driver.find_element_by_xpath("//*[@id='EmployeeEducation_submit']/div/div[7]/div[1]/button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='FI'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Sign out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
