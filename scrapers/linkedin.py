import os
from time import sleep
from turtle import rt
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")

# Retrieve email from environment variables
EMAIL = os.getenv('LINKEDIN_EMAIL')
PASSWORD = os.getenv('LINKEDIN_PASSWORD')

# Wait for page to load
sleep(3)
print('Logging in...')

# Find and input email and password
driver.find_element(By.ID, 'username').send_keys(EMAIL)
driver.find_element(By.ID,'password').send_keys(PASSWORD)

# Submit login form
driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()

# Wait for page to load 
sleep(3)
print('Successfully Logged In...')

driver.get('https://www.linkedin.com/jobs/search/?f_TPR=r604800&geoId=101165590&keywords=junior%20software%20engineer&location=United%20Kingdom')

jobs_list = driver.find_elements(By.CLASS_NAME, 'occludable-update')


for job in jobs_list:
    driver.execute_script("arguments[0].scrollIntoView();", job)
    job.click() 
    sleep(3)
    
    [position, company, location] = job.text.split('\n')[:3]
    details = driver.find_element_by_id("job-details").text

    print([position, company, location])
    print(details)