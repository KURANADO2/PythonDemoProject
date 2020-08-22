from bs4 import BeautifulSoup
import requests
import os
import sys
from contextlib import closing


class WebSpider:
    def __init__(self):
        self.url = 'https://www.ted.com/talks'
        self.imgs = []
        self.authors = []
        self.titles = []
        self.links = []

    def get_talks_links(self):
        response = requests.get(self.url)
        bs = BeautifulSoup(response.text, features='html.parser')
        browse_results = bs.find(name='div', id='browse-results')

        images = browse_results.find_all(name='img')
        for item in images:
            self.imgs.append(item.get('src') + '\n')

        media__message = browse_results.find_all(name='div', class_='media__message')
        for item in media__message:
            self.authors.append(item.find(name='h4', class_='h12 talk-link__speaker').string + '\n')
            self.titles.append(item.find(name='a').string)
            self.links.append(item.find(name='a').get('href') + '\n')

    @staticmethod
    def write_file(cls, text, path):
        with open(path, mode='a', encoding='utf-8') as file:
            file.writelines(text)

    def download_file(self, path, image_url, filename):
        image_path = os.path.join(path, filename)
        request_headers = {'Accept': '*/*',
                           'Accept-Encoding': 'gzip, deflate, br',
                           'Accept-Language': 'zh-CN,zh;q=0.9',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        size = 0
        with closing(requests.get(image_url, headers=request_headers, stream=True)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                sys.stdout.write(filename + ' downloading...\n')
                sys.stdout.write('File Size: %0.2f MB\n' % (content_size / chunk_size / 1024))

                with open(image_path, 'wb') as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        file.flush()
                        sys.stdout.write('In Progress: %.2f%%' % float(size / content_size * 100) + '\r')
                        sys.stdout.flush()

    def start_download(self, imgs):
        for img in imgs:
            file_name = img.split('/')[-1]
            file_name = file_name.split('?')[-2]
            self.download_file('C://Users/Administrator/Desktop//images', img, file_name)


if __name__ == '__main__':
    spider = WebSpider()
    spider.get_talks_links()
    spider.start_download(spider.imgs)
    spider.write_file(WebSpider, spider.imgs, 'C://Users/Administrator/Desktop/imgs.txt')
    spider.write_file(WebSpider, spider.authors, 'C://Users/Administrator/Desktop/authors.txt')
    spider.write_file(WebSpider, spider.titles, 'C://Users/Administrator/Desktop/titles.txt')
    spider.write_file(WebSpider, spider.links, 'C://Users/Administrator/Desktop/links.txt')
