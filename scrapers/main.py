from indeed import scrape_indeed
from linkedin import scrape_linkedin
from glassdoor import scrape_glassdoor

i = 0
while i <= 50:
    scrape_indeed(i)
    i += 10
