import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/bin/GeckoDriverManager().install()'.install())



    def test_search_location_successful(self):
        """ Test searching a valid location """
        driver = self.driver
        driver.get("https://newswire.storyful.com/")
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[normalize-space()="APAC"]')))
        search_input.send_keys('APAC' + Keys.RETURN)
        # If results are shown or If there is a search is confirmed/successful
        result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//span[normalize-space()="APAC Only"]')))
        self.assertTrue('APAC' in result.text)

    def test_search_location_unsuccessful(self):
        """ Test searching an invalid location or  not in the database """
        driver = self.driver
        driver.get("https://newswire.storyful.com/")
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, '//div[contains(@data-cy,"location-filter-pill")]'))) # Assuming the search input has an ID
        search_input.send_keys("**@@!!11" + Keys.RETURN)
        # Assume no results are found
        no_result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, '//input[@id="__next"]')))
        self.assertTrue('No results found' in no_result.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
# The test_search_location_successful method tests the search_location function with a valid location.
# The test_search_location_unsuccessful method tests the search_location function with an invalid location.
# The tearDown method closes the browser after the tests are completed.
# The main method runs the tests when the script is executed.