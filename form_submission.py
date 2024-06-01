from selenium import webdriver 
import time
import random
from selenium.webdriver.common.by import By
from decouple import config

# Function to generate a random date in the format YYYY-MM-DD
def generate_random_date():
    year = random.randint(1990, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  
    return f"{year:04d}-{month:02d}-{day:02d}"

def Form_Submission():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
    time.sleep(2)
    driver.maximize_window()

    # Fill the form fields
    fields = driver.find_elements(By.XPATH, '//*[@id="mG61Hd"]//input')

    verification_code_element = driver.find_element(By.XPATH, '//*[@id="i30"]/span[1]/b')
    # Fill the verification code field
    verification_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    verification_field.send_keys(verification_code_element.text)

    for field in fields:  
        # Skip the verification code field
        if field.get_attribute('value'):
            continue
        field_type = field.get_attribute('type')
        if field_type == 'text':
            field.send_keys("test")
        elif field_type == 'date':
            field.send_keys(generate_random_date())

    text_areas = driver.find_elements(By.XPATH, '//*[@id="mG61Hd"]//textarea')
    for text_area in text_areas:
        text_area.send_keys("test")

    time.sleep(10)
    submit_btn = driver.find_element(By.XPATH, "//div[contains(@role, 'button')]")
    submit_btn.click()

    driver.save_screenshot("form_screenshot.png")
