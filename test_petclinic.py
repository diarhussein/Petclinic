import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PetclinicTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=) # Update the path to your driver

        self.service = Service(executable_path='/usr/local/bin/chromedriver')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options = self.options)

    def test_home_page(self):
        self.driver.get('http://localhost:8080/petclinic/')
        title = self.driver.title
        self.assertEqual(title, "Petclinic Home Page") # Update with your actual title

    def test_find_owners_page(self):
        self.driver.get('http://localhost:8080/petclinic/owners/find')
        # You can add additional checks here, such as searching for an owner and verifying the results

    def test_veterinarians_page(self):
        self.driver.get('http://localhost:8080/petclinic/vets')
        # You may want to add checks here to verify specific content on the Veterinarians page

    def test_error_page(self):
        self.driver.get('http://localhost:8080/petclinic/oups')
        # Add checks to verify the error message or other content on the error page

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
