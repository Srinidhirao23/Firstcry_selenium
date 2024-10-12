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
    
    # Close any popups if present
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='close-popup']"))
        )
        close_button.click()
        print("Closed popup.")
    except Exception as e:
        print("No popup to close or it took too long.")
    
    # Click on the 'Login' button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".poplogin_main"))
    )
    login_button.click()
    print("Clicked on 'Login' button.")
    
    # Click on the 'Login with Facebook' button
    facebook_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wtslogo_block > img:nth-child(1)"))
    )
    facebook_login_button.click()
    print("Clicked on 'Login with Facebook' button.")
    
    # Switch to Facebook login window
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to Facebook login window.")
    
    # Wait for the email input field to be present (if needed)
    email_input_locator = (By.CSS_SELECTOR, "input[name='email']")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(email_input_locator)
    )
    print("Email input field is present.")
    
    # Enter Facebook email or phone number
    email_input = driver.find_element(*email_input_locator)
    email_input.clear()
    email_input.send_keys("8050675891")
    print("Entered Facebook email/phone.")
    
    # Wait for the password input field to be present
    password_input_locator = (By.CSS_SELECTOR, "input[name='pass']")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(password_input_locator)
    )
    print("Password input field is present.")
    
    # Enter Facebook password
    password_input = driver.find_element(*password_input_locator)
    password_input.clear()
    password_input.send_keys("23@chini")
    print("Entered Facebook password.")
    
    # Submit the login form
    login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
    login_button.click()
    print("Clicked on 'Log In' button.")

    print("Login successful.")
    
    
except Exception as e:
    # Print failure message and exception details
    print("Failure in logging in.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(5)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")
