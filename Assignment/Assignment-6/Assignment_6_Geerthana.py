# Author: Geerthana Kannan
# Date: 05-14-2016
# Assignment 6 - To test 8 links
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
                "Educational Diagnostic Center" : "De Anza College :: Educational Diagnostic Center :: Home",
                "Equity, Social Justice and Multicultural Education" : "De Anza College :: Office of Equity :: Home", 
                "Emergency Information" : "De Anza College :: Emergency Information :: Home", 
                "Employment" : "De Anza College :: About De Anza :: Job Opportunities", 
                "Engineering Department" : "De Anza College :: Engineering :: Home", 
                "English Department" : "De Anza College :: English :: Home", 
                "English as a Second Language" : "De Anza College :: English as a Second Language (ESL) :: Home", 
                "Environmental Studies Department" : "De Anza College :: Environmental Studies :: Home",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
