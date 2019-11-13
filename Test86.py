# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test86(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_86(self):
        driver = self.driver
        driver.get("http://localhost/dashboard/icehrm/app/login.php")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Remember me'])[1]/following::button[1]").click()
        driver.find_element_by_id("usersLink").click()
        driver.find_element_by_xpath("//*[@id='User']/div[1]/div/button").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("crp987")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("crprajapati111@gmail.com")
        driver.find_element_by_id("user_level").click()
        driver.find_element_by_id("user_level").click()
        select1 = Select(driver.find_element_by_id("user_level"))
        select1.select_by_visible_text('Manager')
        select2 = Select(driver.find_element_by_xpath("//*[@id='user_roles']"))
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id='s2id_user_roles']").send_keys("Report Manager")
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
