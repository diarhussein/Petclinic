import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class PetclinicTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=) # Update the path to your driver

        self.service = Service(executable_path='/usr/local/bin/chromedriver')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options = self.options)

    def test_home_page(self):
        self.driver.get('http://localhost:8080/petclinic/')
        title = self.driver.title
        self.assertEqual(title, "Home") # Update with your actual title
