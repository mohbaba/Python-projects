import requests
from bs4 import BeautifulSoup

page_url = 'https://www.politifact.com/'
page = requests.get(page_url)

authors = []
date = []
statement = []
sources = []
truth_meter = []

soup = BeautifulSoup(page.content, "html.parser")
ig_posts = soup.find_all("div", class_= 'm-statement__quote')# Statement location
images = soup.find_all("div", class_ = 'm-statement__meter')
footer = soup.find_all("footer", class_ ='m-statement__footer')
meta_source = soup.find_all("a", class_= "m-statement__name")
true_news = soup.find_all("div", class_ = 'm-statement__content')


# python_job_element = [h2_element.parent.parent.parent for h2_element in python_jobs]
for posts in ig_posts:
    post = posts.find("a")
    print(post.text.strip())
    print()
image_sources = []
true_content = []
for item in images:
    image_sources.append(item.get('src'))
    for pics in image_sources:
        if pics == 'https://static.politifact.com/politifact/rulings/meter-mostly-true.jpg':
            true_content.append(pics)
print(true_content)

    
def scrape():
    page_url = 'https://www.politifact.com/'
    page = requests.get(page_url)
    
    for contents in footer:
        details = contents.text.strip()
        content = details.split()
        first_name = content[1]
        last_name = content[2]
        month = content[4]
        day = content[5]
        year = content[6]
        name = first_name + ' '+last_name
        new_date = month+ ' ' +day+ ' '+year
        authors.append(name)
        date.append(new_date)
        
    for posts in ig_posts:
        link = posts.find_all("a")
        post = link[0].text.strip()
        statement.append(post)
        # print(post.text.strip())
        # print()
        
    for s in meta_source:
        word = s.find_all("a")
        word_text = word[0].text.strip()
        sources.append(word)
        
    for i in images:
        facts = i.find("div", class_ = 'c-image').find('img').get('alt')
        truth_meter.append(facts)
