'''
@Description: 多线程爬虫
@Author: Levin-e
@Date: 2020-03-23 22:31:38
'''

import math
import re
import threading
import time
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

import requests
from bs4 import BeautifulSoup
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36 Edg/80.0.361.54'
}


def get_info(url):
    html = get_html(url)
    selector = etree.HTML(html)
    info = selector.xpath('//div[@id="dinfo"]/span/text()')
    pic_num = re.findall(r'\d+', info[0])
    page_num = math.ceil(int(pic_num[0])/3)
    print('该套图总共有%s张' % pic_num[0])
    print('该套图总共有%d页' % page_num)
    return page_num


def get_html(url):
    index = requests.get(url, headers=header)
    return index.text


def get_href(url):  # 获取图片下载地址
    html = get_html(url)
    selector = etree.HTML(html)
    data = selector.xpath('//ul/img/@src')
    for url in data:
        url = url.replace('/s', '')
    start_thread_save_img(data)   # 调用多线程的函数


def save_img(img_src):
    img_src = img_src.replace('/s', '')
    print("正在下载 ->", img_src)
    urllib.request.urlretrieve(
        img_src, 'E:/photo/%s' % img_src.split('/')[-1])
    # 地址格式记得更改，按照下面的例子自己替换，找个文件夹存放你的图
    # 地址不存在是会报错的！！！
    # 示例： E:/photo/


def start_thread_save_img(img_url_list):
    pool = ThreadPool(3)  # 一页三张图，选三就行了，大于这个数值是浪费的
    pool.map(save_img, img_url_list)
    pool.close()


def main():
    url = "https://www.nvshens.net/g/30991/"  # 目标网站的地址格式，千万要注意第一页和之后的页是不一样的
    info = get_info(url)
    start_time = time.time()
    get_href(url)
    second_url = "https://www.nvshens.net/g/30991/{}.html"  # 上下都需要改地址
    for i in range(2, info+1):  # 如果下载到一半失败了，自己在这动手改页码继续下吧。。。
        get_href(second_url.format(i))
        time.sleep(2)  # 这个数值不要太小，对别人的服务器好点，留点喘息的时间
    end_time = time.time()
    print("共耗时：", end_time-start_time)


if __name__ == '__main__':
    main()
