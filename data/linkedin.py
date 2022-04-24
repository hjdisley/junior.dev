import os
from time import sleep
from utils import get_data
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

load_dotenv()

def login_linkedin():
    '''
    Logs in to LinkedIn in order to gain access to the jobs page for scraping
    '''
    try:
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)

        driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")

        # Retrieve email and password from environment variables
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

        scrape_linkedin('https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=101165590&keywords=junior%20software%20engineer&location=United%20Kingdom')

        driver.quit()
    except Exception as e: 
        print('Error logging in ->', e)

def scrape_job_page(job_page_url):
    print(job_page_url)

def scrape_linkedin(url):
    linkedin = get_data(url)

    linkedin_soup = BeautifulSoup(linkedin, 'html.parser')
    linkedin_results = linkedin_soup.find('ul', {'class': 'jobs-search__results-list'}).find_all('li')
   
    job_urls = []
    for job_link in linkedin_results: 
        individual_job_url = job_link.find('a', {'class': 'base-card__full-link'})['href']
        job_urls.append(individual_job_url)

    
    for url in job_urls:
        scrape_job_page(url)
        
login_linkedin()