import requests     # 发送网络请求
import parsel       # 解析数据
import csv          # 保存数据
from fake_useragent import UserAgent
import pandas as pd

path = r"C:\Users\DM\Desktop\Try\dcd.csv"
csv_dcd = open(path, mode='a', encoding='utf-8-sig', newline='')
csv_write = csv.writer(csv_dcd)
csv_write.writerow(['品牌', '车龄', '里程(万公里)', '城市', '认证', '售价(万元)', '原价(万元)', '链接'])

for page in range(1, 5):
    # 1. 找到 目标网址
    url = f'https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x?sh_city_name=%E5%85%A8%E5%9B%BD&page={page}'
    headers = {
    "User-Agent" : UserAgent().chrome #chrome浏览器随机代理
    }
    # 2. 发送请求
    # 3. 获取数据 html网页源代码
    # <Response [200]>: 请求成功的状态码 访问这个网站成功了
    html_data = requests.get(url, headers = headers).text
    # 4. 解析数据 re css xpath bs4 ...
    selector = parsel.Selector(html_data)
    # get(): 获取一个
    # getall(): 获取全部
    lis = selector.css('#__next > div:nth-child(2) > div.new-main.new > div > div > div.wrap > ul li')
    for li in lis:
        # 二次提取
        # ::text： 提取文本内容
        # 品牌
        title = li.css('a dl dt p::text').get()
        # 信息 年份 里程 城市
        # :nth-child(2)：伪类选择器
        info = li.css('a dl dd:nth-child(2)::text').getall()
        # info  列表里面有两个元素
        # 列表合并为字符串
        info_str = ''.join(info)
        # 字符串的分割
        info_list = info_str.split('|')
        car_age = info_list[0]
        mileage = info_list[1].replace('万公里', '')
        city = info_list[2].strip()
        # 链接
        link = 'https://www.dongchedi.com' + li.css('a::attr(href)').get()
        dds = li.css('a dl dd')
        # 如果当前 有 4个dd标签
        if len(dds) == 2:
            # 懂车帝认证
            dcd_auth = li.css('a dl dd:nth-child(3) span::text').get()
            price = li.css('a dl dd:nth-child(4)::text').get()
            original_price = li.css('a dl dd:nth-child(5)::text').get()
        else:
            dcd_auth = '无认证'
            price = li.css('a dl dd:nth-child(3)::text').get()
            original_price = li.css('a dl dd:nth-child(4)::text').get()
        # price = price.replace('万', '')
        original_price = original_price.replace('新车含税价: ', '').replace('万', '')
        print(title, car_age, mileage, city, dcd_auth, price, original_price, link)
        csv_write.writerow([title, car_age, mileage, city, dcd_auth, price, original_price, link])
csv_dcd.close()