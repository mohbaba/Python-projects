import requests
from bs4 import BeautifulSoup

page_url = 'https://www.politifact.com/'
page = requests.get(page_url)

soup = BeautifulSoup(page.content, "html.parser")
