from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Test Case 1: Search and Add to Cart
    driver.get("https://www.firstcry.com/")
    print("Navigated to FirstCry homepage.")

    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='close-popup']"))
        )
        close_button.click()
        print("Closed popup.")
    except Exception as e:
        print("No popup to close or it took too long.")

    search_input_locator = (By.ID, "search_box")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_input_locator)
    )
    print("Search input field is present.")

    input_element = driver.find_element(*search_input_locator)
    input_element.clear()
    input_element.send_keys("baby products" + Keys.ENTER)
    print("Performed search for 'baby products'.")

    search_result_locator = (By.CSS_SELECTOR, "div.list_block:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_result_locator)
    )
    print("Search results are loaded.")

    product_image = driver.find_element(*search_result_locator)
    product_image.click()
    print("Clicked on the first product image link.")

    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to new tab.")

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".div-add-to-cart > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)"))
    )
    add_to_cart_button.click()
    print("Clicked on 'Add to Cart' button.")
    print("Product added to cart successfully!")

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".prodQuant"))
    )
    cart_button.click()
    print("Navigated to cart page.")

    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.remove:nth-child(2)"))
    )
    remove_button.click()
    print("Clicked on 'Remove' button.")
    print("Product removed from cart successfully!")

    # Test Case 2: Add to Shortlist
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_input_locator)
    )
    input_element = driver.find_element(*search_input_locator)
    input_element.clear()
    input_element.send_keys("baby products" + Keys.ENTER)
    print("Performed search for 'baby products'.")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_result_locator)
    )
    print("Search results are loaded.")
    product_image = driver.find_element(*search_result_locator)
    product_image.click()
    print("Clicked on the first product image link.")

    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to new tab.")

    add_to_shortlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#shortlist"))
    )
    add_to_shortlist_button.click()
    print("Clicked on 'Add to Shortlist' button.")
    print("Product added to shortlist successfully!")

    # Test Case 3: Sort by Price High to Low
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_input_locator)
    )
    input_element = driver.find_element(*search_input_locator)
    input_element.clear()
    input_element.send_keys("baby products" + Keys.ENTER)
    print("Performed search for 'baby products'.")

    dropdown_locator = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(dropdown_locator)
    )
    dropdown_element = driver.find_element(*dropdown_locator)
    dropdown_element.click()
    print("Opened sort dropdown.")

    high_to_low_option_locator = (By.CSS_SELECTOR, "li.shortby:nth-child(4) > a:nth-child(1)")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(high_to_low_option_locator)
    )
    high_to_low_option = driver.find_element(*high_to_low_option_locator)
    high_to_low_option.click()
    print("Selected 'Price: High to Low' from the dropdown.")

    time.sleep(5)

    # Test Case 4: Login with Facebook
    driver.get("https://www.firstcry.com/")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".poplogin_main"))
    )
    login_button.click()
    print("Clicked on 'Login' button.")

    facebook_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".wtslogo_block > img:nth-child(1)"))
    )
    facebook_login_button.click()
    print("Clicked on 'Login with Facebook' button.")

    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to Facebook login window.")

    email_input_locator = (By.CSS_SELECTOR, "input[name='email']")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(email_input_locator)
    )
    print("Email input field is present.")

    email_input = driver.find_element(*email_input_locator)
    email_input.clear()
    email_input.send_keys("8050675891")
    print("Entered Facebook email/phone.")

    password_input_locator = (By.CSS_SELECTOR, "input[name='pass']")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(password_input_locator)
    )
    print("Password input field is present.")

    password_input = driver.find_element(*password_input_locator)
    password_input.clear()
    password_input.send_keys("23@chini")
    print("Entered Facebook password.")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
    login_button.click()
    print("Clicked on 'Log In' button.")
    print("Login successful.")

    # Test Case 5: Navigate and Click Categories
    driver.switch_to.window(driver.window_handles[0])

    # Boy Fashion
    BOY_FASHION = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[2]"))
    )
    ActionChains(driver).move_to_element(BOY_FASHION).perform()
    time.sleep(2)

    boy_tshirts = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[3]/div/div/ul[1]/li[3]/a"))
    )
    boy_tshirts.click()
    print("Clicked on Boys Fashion T-shirts button.")

    BOY_FASHION = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[2]"))
    )
    ActionChains(driver).move_to_element(BOY_FASHION).perform()
    time.sleep(2)

    boy_sunglasses = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[3]/div/div/ul[2]/li[10]/a"))
    )
    boy_sunglasses.click()
    print("Clicked on Boys Fashion Sunglasses button.")

    # Girl Fashion
    GIRL_FASHION = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[3]"))
    )
    ActionChains(driver).move_to_element(GIRL_FASHION).perform()
    time.sleep(2)

    girl_frocks = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[4]/div/div/ul[1]/li[2]/a"))
    )
    girl_frocks.click()
    print("Clicked on Girls Fashion Frocks & Dresses button.")

    GIRL_FASHION = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[3]"))
    )
    ActionChains(driver).move_to_element(GIRL_FASHION).perform()
    time.sleep(2)

    girl_ethnic_wear = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[4]/div/div/ul[1]/li[9]/a"))
    )
    girl_ethnic_wear.click()
    print("Clicked on Girls Fashion Ethnic Wear button.")

    # Return to the homepage
    driver.get("https://www.firstcry.com/")
    print("Returned to FirstCry homepage.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver
    driver.quit()
    print("Driver closed.")
