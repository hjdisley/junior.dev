import json
from os import link
from bs4 import BeautifulSoup
import requests

def get_data(url):
    r = requests.get(url)
    return r.content

def get_long_description(individual_job_page):
    pass

def scrape_indeed(page):
    indeed = get_data(f"https://uk.indeed.com/jobs?q=junior%20developer&l=united%20kingdom&fromage=7start={page}")

    indeed_soup = BeautifulSoup(indeed, "html.parser")

    indeed_results = indeed_soup.find(id='resultsCol')

    indeed_jobs = indeed_results.find_all('div', class_='job_seen_beacon')

    job_data = []
    for job in indeed_jobs:
            

        try:
            job_salary = job.find('div', class_='salary-snippet').text
        except:
            job_salary = 'No Salary Specified'

        try:
            if job_title.text[0:3] == 'new':
                job_title = job_title.text[3:len(job_title.text)]
            else:
                job_title = job_title.text
        except: 
            job_title = 'No Title Specified'

        try:
            job_company = job.find('span', class_='companyName').text 

        except:
            job_company = 'No Company Specified'
        
        try:
            job_location = job.find('div', class_='companyLocation').text

        except:
            job_location = 'No Location Specified'

        try:
            job_desc = job.find('div', class_='job-snippet').text
        except:
            job_desc = 'No Description Specified'

        job_data.append({
            "title": job_title,
            "company": job_company,
            "location": job_location,
            "salary": job_salary,
            "description": job_desc
        })

        print(job_data)

scrape_indeed(10)






