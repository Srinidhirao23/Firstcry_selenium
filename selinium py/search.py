from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to Firstcry homepage
    driver.get("https://www.firstcry.com/")
    print("Navigated to Firstcry homepage.")
    
    # Close any popups if present
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='close-popup']"))
        )
        close_button.click()
        print("Closed popup.")
    except Exception as e:
        print("No popup to close or it took too long.")
    
    # Wait for the search input field to be present
    search_input_locator = (By.ID, "search_box")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_input_locator)
    )
    print("Search input field is present.")
    
    # Find the search input field and perform a search
    input_element = driver.find_element(*search_input_locator)
    input_element.clear()
    input_element.send_keys("baby products" + Keys.ENTER)
    print("Performed search for 'baby products'.")
    
    # Wait for search results to be loaded
    search_result_locator = (By.CSS_SELECTOR, "div.list_block:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_result_locator)
    )
    print("Search results are loaded.")
    
    # Click on the first product image in the search results
    product_image = driver.find_element(*search_result_locator)
    product_image.click()
    print("Clicked on the first product image link.")
    
    # Print a message indicating successful search and click
    print("Successful search and click!")
    
except Exception as e:
    # Print failure message and exception details
    print("Failure in search or click process.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(10)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")
