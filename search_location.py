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
service = Service(executable_path='/bin/GeckoDriverManager().install()', port=4444)
driver = webdriver.Firefox(options=options, service=service)
driver.get("https://newswire.storyful.com/")
def select_location(driver, location_tags):
    """
    Selects location tags within the search modal.

    Args:
    driver: Instance of WebDriver.
    location_tags: List of location tags to be selected like ['AFRICA', 'APAC'].
    """
    try:
        # Wait for the modal to be visible and interactable
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-content"))
        )

        # Loop through each tag and click on it
        for tag in location_tags:
            tag_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{tag}')]"))
            )
            tag_element.click()

        # Click the apply button
        apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
        apply_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    driver = webdriver.Firefox(executable_path='/bin/GeckoDriverManager().install()', service=service)
    driver.get("https://newswire.storyful.com/")
    try:
        # Assuming login and navigation to the modal has been handled
        select_location(driver, ['AFRICA', 'APAC', 'EUROPE', 'MIDDLE EAST', 'NORTH AMERICA', 'LATIN AMERICA'])

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
