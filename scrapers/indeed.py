import json
from os import link
from bs4 import BeautifulSoup
import requests

def get_data(url):
    r = requests.get(url)
    return r.content

def get_page_data_and_desc(page):
    indeed = get_data(f"https://uk.indeed.com/jobs?q=junior%20developer&l=united%20kingdom&fromage=7start={page}")

    indeed_soup = BeautifulSoup(indeed, "html.parser")

    try:
        job_desc = indeed_soup.find(id="jobDescriptionText")
        job_desc = job_desc.text.replace('\n', ' ').replace('\r', '')
    except:
        job_desc = "No Description Specified"

    return indeed_soup, job_desc

def scrape_job_result(job_data):
    try:
        job_title = job_data.find("h2", class_="jobTitle").get_text()
    except:
        job_title = "No Job Title Specified"
    
    try:
        job_company = job_data.find("span", class_="companyName").get_text()
    except:
        job_company = "No Company Specified"

    try:
        job_location = job_data.find("div", class_="companyLocation")
    except:
        job_location = "No Location Specified"
    
    try:
        job_salary = job_data.find("div", class_="metadata salary-snippet-container").get_text()
    except:
        job_salary = "Not Specified"
    
    return job_title, job_company, job_location, job_salary

def scrape_full_job_page(page_html):
    pass

def scrape_indeed():
    pass    





