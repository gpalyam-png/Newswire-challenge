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
#service = Service(executable_path=GeckoDriverManager().install(), port=4444)
#driver = webdriver.Firefox(options=options, service=service)


def add_to_favorites(driver, story_identifier):
    """
    Adds a story to favorites based on the story's visible text.

    Args:
    driver: Instance of WebDriver.
    story_identifier: Text that uniquely identifies the story.
    """
    try:
        # Wait for all stories to be loaded on the page
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.story-container"))
        )

        # Find the story by part of its visible text and click the associated save button
        stories = driver.find_elements(By.CSS_SELECTOR, "div.story-container")
        for story in stories:
            if story_identifier in story.text:
                # Find the save button within the specific story element
                save_button = story.find_element(By.CSS_SELECTOR, "button.save-button")  # Assuming the save button is a direct child of the story element
                save_button.click()
                print(f"Story '{story_identifier}' added to favorites.")
                return
        else:
            print(f"Story with identifier '{story_identifier}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    driver = webdriver.Firefox(executable_path='/bin/GeckoDriverManager().install())
    driver = webdriver.Firefox(options=options, service=service)
    driver.get("http://newswire.storyful.com")

    try:
        # Login or navigate as necessary
        add_to_favorites(driver, "Editor's Pick")
    finally:
        # Clean up by closing the browser
        driver.quit()

if __name__ == "__main__":
    main()
