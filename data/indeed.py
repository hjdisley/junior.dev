import json
from bs4 import BeautifulSoup
from utils import get_data
import time

def get_individual_page_description(individual_job_page):
    '''
    Takes in the tag of an individual job page and uses it to make a request to that page.
    From there the function finds and returns the long job description of that pages.
    input:
        individual_job_page (str): string of the job reference
    output:
        long_desc (str): Grabs the long description from the individual job page.
    '''
    link = 'https://uk.indeed.com/viewjob?jk=' + individual_job_page
    html = get_data(link)
    individual_page_soup = BeautifulSoup(html, 'html.parser')

    long_desc = individual_page_soup.find(id='jobDescriptionText').text.replace('\n', ' ').replace('\r', '')

    return long_desc

def scrape_indeed(page):
    '''
    Takes a page number and calls get_data to make a request to that page.
    Then scrapes and returns various pieces of data from that page.
    input:
        page (num): page of indeed to scrape (page 1 = 10, page 2 = 20...).
    output:
        job_data (list): Returns JSON of data scraped from the pages the function is given.

    '''
    print(f'Scraping Indeed Page {int(page/10)}...')
    indeed = get_data(f'https://uk.indeed.com/jobs?q=junior%20developer&l=united%20kingdom&fromage=7start={page}')

    indeed_soup = BeautifulSoup(indeed, 'html.parser')
    indeed_results = indeed_soup.find(id='resultsCol')
    indeed_jobs = indeed_results.find_all('a', class_='tapItem')

    job_data = []
    for job in indeed_jobs:
            try:
                job_salary = job.find('div', {'class':'metadata salary-snippet-container'}).get_text().encode('ascii', 'ignore')
            except:
                job_salary = 'No Salary Specified'

            try:
                job_title = job.find('h2', {'class':'jobTitle'}).get_text()
            except: 
                job_title = 'No Title Specified'

            try:
                job_company = job.find('span',{'class':'companyName'}).get_text() 
            except:
                job_company = 'No Company Specified'
            
            try:
                job_location = job.find('div', {'class':'companyLocation'}).get_text()
            except:
                job_location = 'No Location Specified'
            
            try: 
                short_desc = job.find('div', {'class': 'job-snippet'}).get_text().strip()
            except:
                short_desc = 'No Short Description Specified'

            try:
                individual_job_tag = job.get('id').split('_')[1]
                long_desc = get_individual_page_description(individual_job_tag)
                long_desc.encode('ascii', 'ignore')
            except:
                long_desc = 'No Long Description Specified'
            
            try:
                job_ref = job.get('id').split('_')[1]
            except:
                job_ref = 'No Job Reference'

            job_data.append({
                'job_title': job_title,
                'company_name': job_company,
                'location': job_location,
                'salary': job_salary,
                'short_description': short_desc,
                'long_description': long_desc,
                'job_ref': job_ref,
                'site':'Indeed'
            })

            time.sleep(10)

            print(json.dumps(job_data, indent=4, sort_keys=True))

scrape_indeed(10)

