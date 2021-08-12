# 引入request库
import requests

# 引入BeautifulSoup
from bs4 import BeautifulSoup

# 引入 OS
import os

import time

import threading

'''下载页面'''


def download_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text


# 获取图片下载地址
def get_pic_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    '''获取详情页图片列表'''
    content = soup.find(class_="w620 content a_blue_orange")
    p_list = content.find_all('p')
    d = {}
    for i in p_list:
        # 只取图片的
        img = i.find('img')
        if img is not None:
            src = img.get('src')
            # 寻找图片的下个子节点为标题
            text = i.find_next_sibling().get_text()
            if src is not None:
                d[text] = src
    return d


def get_pic(dicts, html):
    '''获取当前页面的图片,并保存'''
    soup = BeautifulSoup(html, 'html.parser')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    article_title = soup.find(class_="article_title").get_text()
    create_dir('pic/{}'.format(article_title))
    for key, value in dicts.items():
        r = requests.get(value, headers=headers)
        # 获取文件扩展名
        ext = value.split('/')[-1].split('.')[-1]
        # 下载文件
        with open('pic/{}/{}'.format(article_title, value.split('/')[-1]), "wb") as f:
            f.write(r.content)
            time.sleep(5)


# 创建目录
def create_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)

# 得到列表的每个详情链接


def get_detail_url(url):
    doman = 'http://www.gouleide.com'
    html = download_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find('div', class_='ny_video a_blue_orange col999').find_all(
        'a', class_='aimg')
    for a in links:
        link = a.get('href')
        url = doman + '/' + link
        html = download_page(url)
        d = get_pic_list(html)
        get_pic(d, html)


# 线程执行内容
def excute(url):
    get_detail_url(url)


def main():
    # excute('http://www.gouleide.com/img-0-2.html')
    create_dir('pic')
    queue = [i for i in range(1, 10)]  # 页数
    threads = []
    while len(queue) > 0:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
            while len(threads) < 5 and len(queue) > 0:  # 设置线程数据为2
                cur_page = queue.pop(0)
                url = 'http://www.gouleide.com/img-0-{}.html'.format(
                    cur_page)
                thread = threading.Thread(target=excute, args=(url,))
                thread.setDaemon(True)
                thread.start()
                print('{}正在下载{}页'.format(
                    threading.current_thread().name, cur_page))
                threads.append(thread)


# 程序运行入口
if __name__ == '__main__':
    main()
