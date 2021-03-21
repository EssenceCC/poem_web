# encoding: utf-8
'''
  @author 李华鑫
  @create 2020-10-08 9:42
  Mycsdn：https://buwenbuhuo.blog.csdn.net/
  @contact: 459804692@qq.com
  @software: Pycharm
  @file: 古诗词.py
  @Version：1.0

'''
"""
https://www.gushiwen.cn/
https://so.gushiwen.cn/shiwen/
"""
import requests
import time
import random
import csv
from lxml import etree

start_url = "https://so.gushiwen.cn/shiwen/"
base_url = "https://so.gushiwen.cn"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

items = []


def parse_url(url):
    """解析url，得到响应内容"""
    # time.sleep(random.random())
    response = requests.get(url=url, headers=headers)
    # 下面四行是自己加的代码
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接


    return response.content.decode("utf-8")


def parse_html(html):
    """使用xpath解析html，返回xpath对象"""
    etree_obj = etree.HTML(html)
    return etree_obj


def get_first_type():
    """获取所有的一级类型"""
    first_type_list = []

    html = parse_url(start_url)
    etree_obj = parse_html(html)

    first_type_name_list = etree_obj.xpath('(//a[contains(@href,"/gushi/")]|//a[contains(@href,"/wenyan/")])/text()')
    first_type_url_list = etree_obj.xpath('(//a[contains(@href,"/gushi/")]|//a[contains(@href,"/wenyan/")])/@href')
    data_zip = zip(first_type_name_list, first_type_url_list)

    for data in data_zip:
        first_type = {}
        first_type["name"] = data[0]
        first_type["url"] = data[1]
        first_type_list.append(first_type)

    return first_type_list


def get_data(first_type):
    """查询数据"""

    # 一级类型url
    url = base_url + first_type["url"]
    first_type_name = first_type["name"]

    # 向一级类型url发送请求获取二级类型数据
    html = parse_url(url)
    etree_obj = parse_html(html)
    div_list = etree_obj.xpath('//div[@class="typecont"]')
    # 二级类型类型数据div
    for div in div_list:
        # 二级类型名称
        second_type_name = div.xpath(".//strong/text()")
        if second_type_name:  # 有的没有二级类型
            second_type_name = second_type_name[0]
        else:
            second_type_name = ""
        # 二级类型下诗词的名称和url
        poetry_name_list = div.xpath(".//span/a/text()")
        poetry_url_list = div.xpath(".//span/a/@href")
        data_zip = zip(poetry_name_list, poetry_url_list)
        for data in data_zip:
            # item是一个诗词数据
            item = {}
            item["first_type_name"] = first_type_name
            item["second_type_name"] = second_type_name
            item["poetry_name"] = data[0]
            # 诗词url
            poetry_url = base_url + data[1]
            html = parse_url(poetry_url)
            etree_obj = parse_html(html)
            # 诗词作者
            poetry_author = etree_obj.xpath('//p[@class="source"]')[0].xpath(".//text()")
            item["poetry_author"] = "".join(poetry_author).strip()
            # 诗词内容
            poetry_content = etree_obj.xpath('//*[@id="contson45c396367f59"]/text()')
            item["poetry_content"] = "".join(poetry_content).strip()
            # 诗词译文和注释
            if etree_obj.xpath('//div[@class="contyishang"]'):  # 有的没有注释
                poetry_explain = etree_obj.xpath('//div[@class="contyishang"]')[0].xpath(".//text()")
                item["poetry_explain"] = "".join(poetry_explain).strip()
            else:
                item["poetry_explain"] = ""
            print(item)
            # 保存
            save(item)


def save(item):
    """将数据保存到csv中"""
    with open("./古诗词.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(item.values())


def start():
    first_type_list = get_first_type()
    for first_type in first_type_list:
        get_data(first_type)


if __name__ == '__main__':
    start()
