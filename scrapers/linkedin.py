from time import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")

# Retrieve email from environment variables
EMAIL = os.getenv('LINKEDIN_EMAIL')
PASSWORD = os.getenv('LINKEDIN_PASSWORD')

# Wait for page to load
time.sleep(5)
print('Logging in...')

# Find and input email and password
driver.find_element(By.ID, 'username').send_keys(EMAIL)
driver.find_element(By.ID,'password').send_keys(PASSWORD)

# Submit login form
driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()

# Wait for page to load 
time.sleep(5)
print('Successfully Logged In...')

# Select the job icon
print('Navigating to job search...')
driver.find_element(By.ID, "ember20").click() 

# Wait for page to load
time.sleep(5)

# Scrape Jobs page
print('Searching for Jobs...')

job_search_box = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')

job_search_box.click()
job_search_box.send_keys('Junior Engineer')

location_search_box = driver.find_element(By.ID, 'jobs-search-box-location-id-ember272')

location_search_box.send_keys('United Kingdom')
location_search_box.send_keys(Keys.ENTER)




