from bs4 import BeautifulSoup
from urllib import request


url = 'file:///C:/Users/Administrator/Desktop/PythonDemoProject/spider/movielist.html'
response = request.urlopen(url)
html = response.read()
html = html.decode('UTF-8')
# print(html)
bs = BeautifulSoup(html, 'html.parser')
name_list = bs.find_all('div', class_='pl2')
# print(name_list)
for item in name_list:
    item_spans = item.find_all('span')
    # print(item.find('a').text)
    print(item_spans[0].string)
