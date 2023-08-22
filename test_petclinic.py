import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="module")
def browser():
    logging.info("Starting the browser")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_navigate_home_page(browser):
    logging.info("Navigating to the home page")
    browser.get("http://localhost:8080/petclinic/")
    assert "Expected Title or Content" in browser.page_source

def test_find_owners(browser):
    logging.info("Finding and clicking on the 'Find Owners' link")
    find_owners_link = browser.find_element(By.XPATH, '//a[contains(@href, "/petclinic/owners/find")]')
    find_owners_link.click()
    assert "Expected Content" in browser.page_source

def test_search_franklin(browser):
    logging.info("Searching for 'Franklin'")
    search_bar = browser.find_element(By.NAME, "lastName")
    search_bar.clear()
    search_bar.send_keys("Franklin")
    search_bar.submit()
    assert "Franklin" in browser.page_source

def test_navigate_veterinarians(browser):
    logging.info("Finding and clicking on the 'Veterinarians' link")
    vets_link = browser.find_element(By.XPATH, '//a[contains(@href, "/petclinic/vets")]')
    vets_link.click()
    assert "Expected Vet Content" in browser.page_source

def test_navigate_oups(browser):
    logging.info("Finding and clicking on the 'oups' link")
    oups_link = browser.find_element(By.XPATH, '//a[contains(@href, "/petclinic/oups")]')
    oups_link.click()
    assert "Expected Oups Content" in browser.page_source


# import logging
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.info("Starting the script")

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')        # Add this line
# chrome_options.add_argument('--disable-dev-shm-usage')  # Add this line
# driver = webdriver.Chrome(options=chrome_options)

# logging.info("Navigating to the home page")
# driver.get("http://localhost:8080/petclinic/")
# time.sleep(5)

# logging.info("Finding and clicking on the 'Find Owners' link")
# find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/owners/find")]')
# find_owners_link.click()
# time.sleep(5)

# logging.info("Searching for 'Franklin'")
# search_bar = driver.find_element(By.NAME, "lastName")
# search_bar.clear()
# search_bar.send_keys("Franklin")
# time.sleep(1)
# search_bar.submit()
# time.sleep(5)

# logging.info("Finding and clicking on the 'Veterinarians' link")
# find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/vets")]')
# find_owners_link.click()
# time.sleep(5)

# logging.info("Finding and clicking on the 'oups' link")
# find_owners_link = driver.find_element(By.XPATH, '//a[contains(@href, "/petclinic/oups")]')
# find_owners_link.click()
# time.sleep(5)

# logging.info("Script finished successfully")
