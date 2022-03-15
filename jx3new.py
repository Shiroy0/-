from bs4 import BeautifulSoup
import requests

maximum_page = 218
keyword = '新服'

urls = ['https://jx3.xoyo.com/announce/index.html?page={}'.format(str(i)) for i in range(1,maximum_page)]

def get_titles(urls, data = None):
    web_data = requests.get(urls)
    soup = BeautifulSoup(web_data.text, "html.parser")
    titles = soup.select(' body > div > div > div > div > div > div > div > div > div > ul > li > a ')
    for title in titles:
        if(keyword in title.get_text()):
            data = {
                'title': title.get_text()
            }
        else:
            continue
        print(data)

for titles in urls:
    get_titles(titles)
