from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
service = webdriver.firefox.service.Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Initialize the WebDriver for Firefox
driver = webdriver.Firefox(executable_path='/bin/GeckoDriverManager().install()', service=service)

# Navigate to the login page
driver.get("http://newswire.storyful.com/")  # Update with the actual URL if different

# Login
try:
    # Wait for the email input to be clickable
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, '//input[@id="user_email"]'))  # Update with actual element details
    )
    email_input.send_keys("geetha.palyam@example.com")

    password_input = driver.find_element(By.ID, '//input[@id="user_password"]')  # Update with actual element details
    password_input.send_keys("Password1@", Keys.RETURN)

    # Search for a location
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="APAC"]'))  # Update with actual element details
    )
    search_field.clear()
    search_field.send_keys("APAC", Keys.RETURN)

    # Save a story
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Save"]'))  # Update with actual element details
    )
    save_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
