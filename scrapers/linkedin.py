import json
from bs4 import BeautifulSoup
from utils import get_data
import time

def scrape_linkedin(page):
    '''
    '''
    linkedin = get_data(f'https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=junior%20engineer&location=United%20Kingdom&start={page}')

    linkedin_soup = BeautifulSoup(linkedin, 'html.parser')
    print(linkedin_soup)
    # indeed_results = linkedin_soup.find('div', {'class': 'jobs-search-two-pane__results'})
    # indeed_jobs = indeed_results.find_all('a', class_='tapItem')



scrape_linkedin(25)