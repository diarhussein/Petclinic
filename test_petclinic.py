import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting the script")

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

logging.info("Navigating to the home page")
driver.get("http://localhost:8080/petclinic/")
time.sleep(5)

logging.info("Finding and clicking on the 'Find Owners' link")
find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/owners/find")]')
find_owners_link.click()
time.sleep(5)

logging.info("Searching for 'Franklin'")
search_bar = driver.find_element(By.NAME, "lastName")
search_bar.clear()
search_bar.send_keys("Franklin")
time.sleep(1)
search_bar.submit()
time.sleep(5)

logging.info("Finding and clicking on the 'Veterinarians' link")
find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/vets")]')
find_owners_link.click()
time.sleep(5)

logging.info("Finding and clicking on the 'oups' link")
find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/oups")]')
find_owners_link.click()
time.sleep(5)

logging.info("Script finished successfully")
