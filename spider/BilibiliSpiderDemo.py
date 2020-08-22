from bs4 import BeautifulSoup
import requests


class BilibiliSpider:
    def __init__(self):
        self.url = 'https://www.bilibili.com/ranking'
        self.list = []

    def get_rank_list(self):
        response = requests.get(self.url)
        bs = BeautifulSoup(response.text, features='html.parser')
        rank_list = bs.find(name='ul', class_='rank-list')
        items = rank_list.find_all(name='li', class_='rank-item')
        for item in items:
            rank = item.find(name='div', class_='num').string
            img = item.find(name='img').get('src')
            title = item.find(name='a', class_='title').string
            play = item.find(name='span', class_='data-box').string
            danmaku = item.find(name='span', class_='data-box').string
            author = item.find(name='span', class_='data-box').string
            score = item.find(name='div', class_='pts').string
            link = item.find(name='a', class_='title').get('href')
            self.list.append(BilibiliRank(rank, img, title, play, danmaku, author, score, link))

    @staticmethod
    def write_file(cls, text, path):
        with open(path, mode='w', encoding='utf-8') as file:
            file.writelines(text)


class BilibiliRank(object):
    def __init__(self, rank, img, title, play, danmaku, author, score, link):
        # 排名
        self.rank = rank
        # 预览图片
        self.img = img
        # 标题
        self.title = title
        # 播放量
        self.play = play
        # 弹幕
        self.danmaku = danmaku
        # UP
        self.author = author
        # 综合得分
        self.score = score
        # 视频地址
        self.link = link


if __name__ == '__main__':
    bilibiliSpider = BilibiliSpider()
    bilibiliSpider.get_rank_list()
    for item in bilibiliSpider.list:
        print('%s %s %s %s %s %s %s %s' %(item.rank, item.img, item.title, item.play, item.danmaku, item.author, item.score, item.link))
    # spider.write_file(WebSpider, spider.imgs, 'C://Users/Administrator/Desktop/imgs.txt')
