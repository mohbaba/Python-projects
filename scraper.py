import requests
from bs4 import BeautifulSoup

page_url = 'https://www.politifact.com/'
page = requests.get(page_url)

soup = BeautifulSoup(page.content, "html.parser")
ig_posts = soup.find_all("div", class_= 'm-statement__quote')
images = soup.find_all("img", class_ = 'c-image__original')


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
# print(image_sources)
    # if item['src'] == ['https://static.politifact.com/politifact/rulings/meter-mostly-true.jpg']:
    #     print(item['src'])