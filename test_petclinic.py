import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path="/usr/local/binchromedriver")
driver = webdriver.Chrome(service=service)


chrome_options = Options()
#chrome_option.add.argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the home page
driver.get("http://localhost:8080/petclinic/")

time.sleep(5)

# Find and click on the 'Find Owners' link
find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/owners/find")]')
find_owners_link.click()

time.sleep(5)

search_bar = driver.find_element(By.NAME, "lastName")
search_bar.clear()
search_bar.send_keys("Franklin")
time.sleep(1)
search_bar.submit()
time.sleep(5)

# Find and click on the 'Veterinarians' link
find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/vets")]')
find_owners_link.click()
time.sleep(5)

# Find and click on the 'Veterinarians' link
find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/oups")]')
find_owners_link.click()
time.sleep(5)