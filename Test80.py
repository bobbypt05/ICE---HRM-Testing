# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test80(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_80(self):
        driver = self.driver
        driver.get("http://localhost/dashboard/icehrm/app/login.php")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Remember me'])[1]/following::span[1]").click()
        driver.find_element_by_xpath('//*[@id="employeeLink"]').click()
        driver.find_element_by_xpath('//*[@id="Employee"]/div[1]/div/button[1]').click()
        driver.find_element_by_id('employee_id').send_keys('EM-135')
        driver.find_element_by_id('first_name').send_keys('ABC')
        driver.find_element_by_id('last_name').send_keys('XYZ')
        select1 = Select(driver.find_element_by_id('nationality'))
        select1.select_by_visible_text('Afghan')
        driver.find_element_by_id('birthday').send_keys('1998-05-09')
        driver.find_element_by_id('joined_date').send_keys('2019-07-20')
        driver.find_element_by_xpath("//*[@id='Employee_submit']/div/div[41]/div[1]/button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="createUserModel"]/div/div/div[3]/button[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='delegationDiv']/nav/div[2]/ul/li[5]/a").click()
        driver.find_element_by_xpath("//*[@id='delegationDiv']/nav/div[2]/ul/li[5]/ul/li[2]/div[2]/a").click()



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
