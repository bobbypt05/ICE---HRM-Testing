# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test59(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_59(self):
        driver = self.driver
        driver.get("http://localhost/dashboard/icehrm/app/login.php")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Remember me'])[1]/following::button[1]").click()
        driver.find_element_by_id("employeeLink").click()
        driver.find_element_by_id("tabEmergencyContact").click()
        driver.find_element_by_xpath("//*[@id='EmergencyContact']/div[1]/div/button[1]").click()
        select1 = Select(driver.find_element_by_id('employee'))
        select1.select_by_visible_text('IceHrm Employee')
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Antony")
        driver.find_element_by_id("mobile_phone").click()
        driver.find_element_by_id("mobile_phone").clear()
        driver.find_element_by_id("mobile_phone").send_keys("9373721976")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Mobile Phone'])[3]/following::button[1]").click()
        time.sleep(2)
        driver.find_element_by_link_text("IceHrm").click()
        driver.find_element_by_link_text("Sign out").click()
        driver.close()
    
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
