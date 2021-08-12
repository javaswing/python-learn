"""
爬取妹子图全网妹子图片，可以选择爬取年份，自动分类保存
"""
import requests
from lxml import etree
# import re
import os
# from time import sleep

class Meizitu(object):
    """爬取妹子图中的图片"""
    def __init__(self, year):
        self.url = "http://www.mzitu.com/all/"
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        self.year = year

    # 获取页面
    def get_page(self, url, headers):
        response = requests.get(url, headers=headers)
        return response.content.decode()

    # 提取列表页中的urls
    def get_detail_urls_list(self, page_content, year):
        html_content = etree.HTML(page_content)
        year_list = html_content.xpath("//div[@class='year']/text()")
        index = 2019 - year
        # 提取某一年的相关主题的urls
        xpath_var = "//div[@class='year'][{}]/following-sibling::*[1]//p[@class='url']/a/@href".format(index)
        if index <= len(year_list):
            urls_list = html_content.xpath(xpath_var)
            # print(urls_list)
        else:
            urls_list = None
        return urls_list
    
    # 构造保存路径并创建目录
    def save_path(self, detail_html_content, first_img_url, img_name):
        # 构造保存路径
        path_prefix1 = detail_html_content.xpath("//div[@class='currentpath']/a/text()")[1]
        # print(path_prefix1)
        path_prefix2 = first_img_url[20:29]
        # print(path_prefix2)
        save_path = "./妹子图/" + path_prefix1 + path_prefix2 + img_name + "/"

        # 如果目录不存在，则创建目录
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        return save_path
    
    # 请求和保存图片
    def save_img(self, img_url, img_headers, img_save_path):
        # 请求图片
        img_content = requests.get(img_url, headers=img_headers).content
        # 保存图片
        with open(img_save_path, "wb") as f:
            f.write(img_content)
    
    # 构造图片请求地址
    def img_url(self, first_img_url, img_index):
        if img_index < 10:
            img_url = first_img_url[:32] + "0" + str(img_index) + ".jpg"
        else:
            img_url = first_img_url[:32] + str(img_index) + ".jpg"
        # print(img_url)
        return img_url
    
    # 构造图片的请求头
    def img_headers(self, url, img_index):
        if img_index == 1 :
            refer_url = url
        else:
            refer_url = url + "/" + str(img_index)
        # print(refer_url)

        img_headers = {
            # "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",
            # "Accept-Encoding":"gzip, deflate",
            # "Accept-Language":"zh-CN,zh;q=0.9",
            # "Connection":"keep-alive",
            "Host":"i.meizitu.net",
            "Referer":refer_url,
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        # print(img_headers,end="\n\n")
        return img_headers

    # 构造每个主题的图片请求地址 并保存
    def get_img_urls(self, url, detail_html_content, first_img_url, img_name, save_path):
        # 每个主题中的图片总数
        img_total_num = int(detail_html_content.xpath("//div[@class='pagenavi']/a/span/text()")[4])
        
        # 构造图片地址 http://i.meizitu.net/2018/02/18c01.jpg
        for img_index in range(1, img_total_num + 1):
            img_url = self.img_url(first_img_url, img_index)
            img_headers = self.img_headers(url, img_index)            
            # 构造图片具体保存路径
            img_save_path = save_path + img_name + str(img_index) + ".jpg"            
            # sleep(10)
            # 请求和保存图片
            self.save_img(img_url, img_headers, img_save_path)

    # 获取图片
    def get_image(self, detail_urls_list):
        for url in detail_urls_list:
            detail_page = self.get_page(url, headers=self.headers)
            detail_html_content = etree.HTML(detail_page)
            # 第一页图片地址
            first_img_url = detail_html_content.xpath("//div[@class='main-image']/p/a/img/@src")[0]
            # print(first_img_url)
            # 获取图片保存的名字
            img_name = detail_html_content.xpath("//h2[@class='main-title']/text()")[0]
            # print(img_name)
            
            # 构建保存路径并创建目录
            save_path = self.save_path(detail_html_content, first_img_url, img_name)

            # 构建图片请求地址并下载
            self.get_img_urls(url, detail_html_content, first_img_url, img_name, save_path)


    # 启动爬虫
    def run_spider(self):
        # 获取妹子图中的列表页内容
        page_content = self.get_page(self.url, self.headers)
        # 获取详情页的地址列表
        detail_urls_list = self.get_detail_urls_list(page_content, self.year)
        # 获取图片
        self.get_image(detail_urls_list)

if __name__ == "__main__":
    year = int(input("请输入您要爬取的年份："))
    meizitu = Meizitu(year)
    meizitu.run_spider()
