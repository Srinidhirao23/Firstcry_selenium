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


# Wait for the 'Boy fashion' button to be present and clickable
        BOY_FASHION = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[2]"))
        )

        ActionChains(driver).move_to_element(BOY_FASHION).perform()
        time.sleep(2) 

        BOY_FASHION = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[3]/div/div/ul[1]/li[3]/a"))
        )
        BOY_FASHION.click()
        print("In Boys Fashion T shirts  button clicked.")

        BOY_FASHION = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[2]"))
        )

        ActionChains(driver).move_to_element(BOY_FASHION).perform()
        time.sleep(2)  

        BOY_FASHION = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[3]/div/div/ul[2]/li[10]/a"))
        )
        BOY_FASHION.click()
        print("Boys Fashion Sunglasses  button clicked.")


# Wait for the 'GIRL fashion' button to be present and clickable
        GIRL_FASHION = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[3]"))
        )

        ActionChains(driver).move_to_element(GIRL_FASHION).perform()
        time.sleep(2)  

        # Wait for the 'Girl fashion' button to be present and clickable
        GIRL_FASHION = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[4]/div/div/ul[1]/li[2]/a"))
        )
        GIRL_FASHION.click()
        print("In Girls Fashion Frocks & Dresses  button clicked.")

        GIRL_FASHION = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[3]"))
        )

        ActionChains(driver).move_to_element(GIRL_FASHION).perform()
        time.sleep(2)  

        GIRL_FASHION = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[4]/div/div/ul[1]/li[10]/a"))
        )
        GIRL_FASHION.click()
        print("Girl Fashion Ethnic  button clicked.")



# Wait for the 'Toys' button to be present and clickable
        TOYS = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[5]/a"))
        )
        ActionChains(driver).move_to_element(TOYS).perform()
        time.sleep(2)  

        TOYS = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[6]/div/div/ul[1]/li[2]/a"))
        )
        TOYS.click()
        print("TOY Musical Toys clicked.")

        TOYS = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[5]/a"))
        )

        ActionChains(driver).move_to_element(TOYS).perform()
        time.sleep(2)  

        TOYS = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[6]/div/div/ul[1]/li[7]/a"))
        )
        TOYS.click()
        print("TOY Sports and Games clicked.")

# Wait for the 'GEAR' button to be present and clickable
        GEAR = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[7]/a"))
        )
        ActionChains(driver).move_to_element(GEAR).perform()
        time.sleep(2)  

        GEAR = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[8]/div/div/ul[1]/li[2]/a"))
        )
        GEAR.click()
        print("GEAR Baby Strollers & Prams clicked.")

        GEAR = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[1]/ul/li[7]/a"))
        )
        ActionChains(driver).move_to_element(GEAR).perform()
        time.sleep(2)  

        GEAR = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[8]/div/div/div[2]/div[8]/div/div/ul[3]/li[2]/a"))
        )
        GEAR.click()
        print("GEAR Battery Operated Ride-Ons clicked.")

#Enter button click on Boys Fashion
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'BOY FASHION')]"))
        )

        language = driver.find_element(By.XPATH, "//*[contains(text(), 'BOY FASHION')]")
        language.click()
        print("Boy Fashion page opened")

#Enter button click on Girl Fashion

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'GIRL FASHION')]"))
        )

        language = driver.find_element(By.XPATH, "//*[contains(text(), 'GIRL FASHION')]")
        language.click()
        print("Girl Fashion page opened")


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
   

finally:
    # Wait for a few seconds to observe the result
    time.sleep(10)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")