import os
from time import sleep
from utils import get_data
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options 
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

    except Exception as e: 
        print('Error logging in ->', e)

    scrape_linkedin('https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=101165590&keywords=junior%20software%20engineer&location=United%20Kingdom')

    driver.quit()

def scrape_job_page(job_page_url):
    individual_job_page = get_data(job_page_url)

    individual_job_page_soup = BeautifulSoup(individual_job_page, 'html.parser')

    job_data = []
    try:
        job_title = individual_job_page_soup.find('h1').get_text()
    except:
        job_title = 'No Title Specified'

    try: 
        job_salary = individual_job_page_soup.find('a', {'class': 'app-aware-link'}).get_text()
    except:
        job_salary = 'No Salary Specified'
    
    try: 
        job_location = individual_job_page_soup.find('span', {'class', 'jobs-unified-top-card__bullet'}).get_text()
    except:
        job_location = 'No Location Specified'

    try:
        job_workplace_type = individual_job_page_soup.find('span', {'class', 'jobs-unified-top-card__workplace-type'}).get_text()
    except:
        job_workplace_type = 'No Workplace Type Specified'
    
    try:
        job_description_long = individual_job_page_soup.find('div', {'class': 'jobs-box__html-content'}).find_all('p')
    except:
        job_description_long = 'No Long Description Specified'
    
    job_data.append({
        'job_title': job_title,
        'job_salary': job_salary,
        'job_location': job_location,
        'job_workplace_type': job_workplace_type,
        'job_description_long': job_description_long
    })

    print(job_data)
    

def scrape_linkedin(url):
    linkedin = get_data(url)

    linkedin_soup = BeautifulSoup(linkedin, 'html.parser')
    linkedin_results = linkedin_soup.find('ul', {'class': 'jobs-search__results-list'}).find_all('li')
   
    job_urls = []
    for job in linkedin_results: 
        individual_job_url = job.find('a', 'base-card__full-link', href=True)['href']

        job_urls.append(individual_job_url)

    for index, url in enumerate(job_urls):
        if index == 0:
            scrape_job_page(url)
        
login_linkedin()