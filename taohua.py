# 引入request库
import requests

# 引入BeautifulSoup
from bs4 import BeautifulSoup

# 引入 OS
import os

import time

import threading


import urllib.error

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
    content = soup.find('td', class_="t_f")
    imgs = content.find_all('img')
    return imgs


def get_pic(imgs, html):
    '''获取当前页面的图片,并保存'''
    soup = BeautifulSoup(html, 'html.parser')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    article_title = soup.find('span', id="thread_subject").get_text()
    create_dir('pic/{}'.format(article_title))
    temp = []
    for img in imgs:
        src = img.get('file')
        temp.append(src)
    # 返回的图片会有一张一样的在这里进行去重
    result = list(set(temp))
    for src in result:
        file_name = src.split('/')[-1]
        print('开始爬取图片：' + file_name)
        try:
            r = requests.get(src, headers=headers, timeout=5)
            if r.status_code == 200:
                # 下载文件
                with open('pic/{}/{}'.format(article_title, src.split('/')[-1]), "wb") as f:
                    f.write(r.content)
                r.close()
                print('爬取完成:{}'.format(file_name))
            else:
                print('图片：{},请求失败'.format(file_name))
        except urllib.error.URLError as e:
            print('下载图片异常：' + e.reason)
        except requests.exceptions.ConnectTimeout:
            print('request请求超时,图片:{}'.format(file_name))
        except requests.exceptions.Timeout:
            print('图片:{},下载超时'.format(file_name))
        except Exception as e:
            print(e)
        print('-------------------------------------------------->')
        time.sleep(10)


# 创建目录
def create_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)

# 得到列表的每个详情链接


def get_detail_url(url):
    doman = 'http://thzu.net/'
    html = download_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find('ul', class_='ml waterfall cl').find_all(
        'a', class_='z')
    for a in links:
        link = a.get('href')
        print('link:' + link)
        url = doman + '/' + link
        html = download_page(url)
        d = get_pic_list(html)
        get_pic(d, html)


def test():
    url = 'http://thzu.net/forum-42-1.html'
    html = download_page(url)
    d = get_pic_list(html)
    get_pic(d, html)

# 线程执行内容


def excute(url):
    get_detail_url(url)


def main():
    excute('http://thzu.net/forum-42-5.html')
    # test()
    # create_dir('pic')
    # queue = [i for i in range(1, 10)]  # 页数
    # threads = []
    # while len(queue) > 0:
    #         for thread in threads:
    #             if not thread.is_alive():
    #                 threads.remove(thread)
    #         while len(threads) < 5 and len(queue) > 0:  # 设置线程数据为2;
    #             cur_page = queue.pop(0)
    #             url = 'http://thzu.net/forum-42-{}.html'.format(
    #                 cur_page)
    #             thread = threading.Thread(target=excute, args=(url,))
    #             thread.setDaemon(True)
    #             thread.start()
    #             print('{}正在下载{}页'.format(
    #                 threading.current_thread().name, cur_page))
    #             threads.append(thread)


# 程序运行入口
if __name__ == '__main__':
    main()
