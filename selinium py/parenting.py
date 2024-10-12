from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to FirstCry homepage
    driver.get("https://www.firstcry.com/")
    print("Navigated to FirstCry homepage.")

    # Close any popups if present (optional)
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='close-popup']"))
        )
        close_button.click()
        print("Closed popup.")
    except Exception as e:
        print("No popup to close or it took too long.")

    # Click on 'FirstCry Parenting' link
    parenting_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[5]/div/div[3]/ul/li[5]/a/span"))
    )
    parenting_button.click()
    print("Clicked on 'FirstCry Parenting'.")

    # Switch to new tab (FirstCry Parenting)
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to 'FirstCry Parenting' tab successfully.")

    # Wait for the Instagram icon to be clickable
    instagram_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/header/div[3]/div/section[1]/div/div/span[2]/a/span"))
    )
    instagram_icon.click()
    print("Clicked on Instagram icon.")

    # Switch to new tab (Instagram)
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to Instagram tab successfully.")

    # Optionally, you can perform further verifications or assertions here
    
except Exception as e:
    # Print failure message and exception details
    print("Failure in automated testing.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(10)

    # Close the browser
    driver.quit()
    print("Browser closed.")
