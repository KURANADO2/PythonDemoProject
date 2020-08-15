from bs4 import BeautifulSoup
import requests


class WebSpider:
    def __init__(self):
        self.url = 'https://www.ted.com/talks'

    def get_talks_links(self):
        response = requests.get(self.url)
        html = response.text
        return html

    def write_file(self, text, path):
        with open(path, mode='a', encoding='utf-8') as file:
            file.writelines(text)


if __name__ == '__main__':
    spider = WebSpider()
    html = spider.get_talks_links()
    spider.write_file(html, 'C://Users/Administrator/Desktop/ted.html')
    print(html)
