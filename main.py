from os import fwalk
import json
from bs4 import BeautifulSoup
from utils import get_data



def scrape_indeed():
    indeed = get_data("https://uk.indeed.com/jobs?q=junior%20developer&l=United%20Kingdom&vjk=c39d433498a57a21")

    soup = BeautifulSoup(indeed, "html.parser")

    indeed_results = soup.find(id='resultsCol')

    indeed_jobs = indeed_results.find_all('div', class_='job_seen_beacon')

    job_data = []
    for job in indeed_jobs:
        job_title = job.find('h2', class_='jobTitle')
        job_company = job.find('span', class_='companyName') 
        job_location = job.find('div', class_='companyLocation')
        job_desc = job.find('div', class_='job-snippet')
        
        try:
            job_salary = job.find('div', class_='salary-snippet').text
        except:
            job_salary = 'Not Specified'

        if job_title.text[0:3] == 'new':
            job_title = job_title.text[3:len(job_title.text)]
        else:
            job_title = job_title.text
        

        job_data.append({
            "title": job_title,
            "company": job_company.text,
            "location": job_location.text,
            "salary": job_salary,
            "description": job_desc.text.strip('\n').strip()
        })



        # f = open('indeed.json',ßß 'x')

        json_string = json.dumps(job_data, indent=4)

        print(json_string)
        # f.write(json_string)
    

def scrape_linkedin():
    pass

def scrape_glassdoor():
    pass

scrape_indeed()