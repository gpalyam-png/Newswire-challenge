import logging  # Import the logging module
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# Configure logging to output to console
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

options = webdriver.FirefoxOptions()
options.log.level = "trace"
# options.headless = True

# Set up Selenium with GeckoDriver on a specific port
service = Service(executable_path=GeckoDriverManager().install(), port=4444)
driver = webdriver.Firefox(options=options, service=service)

driver.get("https://newswire.storyful.com")
try:
    # Use WebDriverWait to wait for a specific element to be loaded
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds before throwing a TimeoutException
    favorite_button = wait.until(EC.presence_of_element_located((By.XPATH, "//body[contains(@data-new-gr-c-s-check-loaded,'8.912.0')]")))
    favorite_button.click()

    # Wait for 2 seconds to see the result of the click, consider using WebDriverWait here as well
    time.sleep(2)  # Consider replacing this with another WebDriverWait for a specific condition

finally:
    # Teardown
    driver.quit()