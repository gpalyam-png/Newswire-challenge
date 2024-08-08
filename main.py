from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from save_story import save_story
from search_location import search_location

service = webdriver.firefox.service.Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Initialize the WebDriver for Firefox
driver = webdriver.Firefox(executable_path='/bin/GeckoDriverManager().install()', service=service)

# Navigate to the login page
url = "http://newswire.storyful.com"

def login(driver, url, email, password):
    """Logs into the website."""
    driver.get("http://newswire.storyful.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '//input[@id="user_email"]')))
    driver.find_element(By.ID, '//input[@id="user_email"]').send_keys(email)
    driver.find_element(By.ID, '//input[@id="user_password"]').send_keys(password + Keys.RETURN)

def save_story(driver, story_identifier):
    """Adds a story to favorites."""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.save-button")))
    save_buttons = driver.find_elements(By.CSS_SELECTOR, "button.save-button")
    # This could be enhanced to find a specific story
    save_buttons[0].click()  # Clicks the first save button found

def search_location(driver, location):
    """Selects a location from a location picker modal."""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.location-search-input")))
    search_input = driver.find_element(By.CSS_SELECTOR, "input.location-search-input")
    search_input.send_keys(location + Keys.RETURN)

def main():
    driver = webdriver.Firefox(executable_path='/bin/GeckoDriverManager().install()',service=service)
    try:
        login(driver, "http://newswire.storyful.com", "geetha@example.com", "Password1@")
        search_location(driver, "APAC")
        save_story(driver, "Editor's Pick")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
