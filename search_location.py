from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.FirefoxOptions()
options.log.level = "trace"
options.headless = True

# Set up Selenium with GeckoDriver on a specific port
service = Service(executable_path=GeckoDriverManager().install(), port=4444)
driver = webdriver.Firefox(options=options, service=service)
driver.get("https://newswire.storyful.com/")
try:
    # Wait until the location picker is clickable
    location_picker = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "//input[@type='text']"))  # Adjust the ID accordingly
    )
    location_picker.click()

    # Select multiple regions, assuming these elements can be selected by name
    regions = ['AFRICA', 'APAC', 'EUROPE', 'MIDDLE EAST', 'NORTH AMERICA', 'LATIN AMERICA']
    for region in regions:
        driver.find_element(By.NAME, "//button[contains(text(),'APAC')]").click()  # Adjust selector method as necessary

    # Apply the selections
    apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]")
    apply_button.click()

    # Optionally, check for some expected result or state to verify the outcome
    # This might be a new page load, a popup, or a specific element's visibility
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "//span[contains(text(),'Europe (+1)')]"))  # Example condition
    )
    print("Test Passed: Locations applied successfully.")

except Exception as e:
    print(f"Test Failed: {str(e)}")
finally:
    driver.quit()