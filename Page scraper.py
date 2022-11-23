import requests
from bs4 import BeautifulSoup

page_url = 'https://realpython.github.io/fake-jobs/'
# page_url= input('Enter the url of the website to be scraped')
page = requests.get(page_url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = 'ResultsContainer')

# this returns a list which can be iterated through
job_elements = soup.find_all("div",class_='card-content')
print(results.text.strip)
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
python_jobs = soup.find_all("h2",string=lambda text: "python" in text.lower())
for jobs in python_jobs:
    job = jobs.find("h2",string=lambda text: "python" in text.lower())
    company = jobs.find("h3", class_="company")
    location = jobs.find("p",class_="location")
python_job_element = [h2_element.parent.parent.parent for h2_element in python_jobs]
for job_element in python_job_element:
    title_element =job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# print(results.prettify())
