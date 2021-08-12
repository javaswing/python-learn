# 引入request库
import requests
from requests import exceptions

# 引入BeautifulSoup
from bs4 import BeautifulSoup

# 引入 OS
import os

import time

import threading

import urllib.error

from urllib.parse import urlparse
import re


'''下载页面'''


def download_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    return r.text


# 获取mv下载地址
def get_mv_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('td', class_="t_f").find('script')
    s = re.search(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', content.get_text())
    if s:
        return s.group()
    else:
        print('没有匹配到http地址')
        return ''


def get_mv(mv_link, html):
    soup=BeautifulSoup(html, 'html.parser')
    article_title=soup.find('span', id="thread_subject").get_text()
    create_dir('mv/{}'.format(article_title))
    print('{}开始下载'.format(article_title))
    file_name=mv_link.split('/')[-1]
    print('开始爬取mv：{}, 地址为：{}'.format(file_name, mv_link))
    # 检测图片是否存在如果存在直接跳过
    if os.path.exists('mv/{}/{}'.format(article_title, mv_link.split('/')[-1])):
        print('mv{} ,已存在,跳过下载！'.format(mv_link.split('/')[-1]))
        print('-------------------------------------------------->')
    try:
        real_src=get_real_pic(mv_link)
        r=requests.get(real_src, headers=img_headers(
            mv_link), timeout=get_timeout(mv_link))
        if r.status_code == 200:
            # 下载文件
            with open('pic/{}/{}'.format(article_title, mv_link.split('/')[-1]), "wb") as f:
                f.write(r.content)
            r.close()
            print('爬取完成:{}'.format(file_name))
        else:
            print('mv{},请求失败'.format(file_name))
    except exceptions.Timeout as e:
        print('请求超时,图片:{}, 原因：{}'.format(file_name, str(e)))
    except exceptions.HTTPError as e:
        print('http请求错误:'+str(e))
    except Exception as e:
        print('程序异常Error：' + str(e))
    print('-------------------------------------------------->')
    time.sleep(3)


''' 由目前的src进行分析并返回可下载的URL地址'''


def get_real_pic(src):
    # TODO 第一种数据格式：/data/attachment/forum/201404/28/100214kjooc7hob4abbobj.jpg ，进行添加域名前缀
    return src

# 根据域名优化下载时间


def get_timeout(url):
    time=10
    domain=get_domain(url)
    if domain == 'www.yuoimg.com' or domain == 'yuoimg.com':
        time=15
    return time


''' 设定请求Img的请求头'''


def img_headers(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    domain=get_domain(url)
    # https://www.yuoimg.com/u/20180922/10241966.jpg 或者 https://yuoimg.com/u/20180926/23520058.jpg  请求头
    if domain == 'www.yuoimg.com' or domain == 'yuoimg.com':
        headers['authority']=domain
        headers['method']='GET'
        headers['path']=urlparse(url).path
        headers['scheme']='https'
        headers['cookie']='__cfduid=dacdbbeb06729375113c4d777fb8c82b41537943877'
        # headers['referer'] = 'http://thzu.net/thread-1879583-1-5.html'
    return headers

# 根据URL获取域名


def get_domain(url):
    """Get domain name from url"""
    parsed_uri=urlparse(url)
    domain='{uri.netloc}'.format(uri=parsed_uri)
    return domain

# 创建目录


def create_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)

# 得到列表的每个详情链接


def get_link_url(url):
    doman=get_domain(url)
    html=download_page(url)
    soup=BeautifulSoup(html, 'html.parser')
    links=soup.find_all('a', class_='s xst', text=re.compile('^(?!赞助详情).*$'))
    for a in links:
        link=a.get('href')
        url=urlparse(url).scheme + "://" + doman + '/' + link
        print(url)
        html=download_page(url)
        link=get_mv_link(html)
        get_mv(link, html)


def test():
    url='http://thzu.net/thread-19363-1-1.html'
    html=download_page(url)
    link=get_mv_link(html)
    get_mv(link, html)

# 线程执行内容


def excute(url):
    get_link_url(url)


def main():
    excute('http://thzu.net/forum-65-1.html')
    #test()
    # create_dir('pic')
    # queue = [i for i in range(1, 5)]  # 页数
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
