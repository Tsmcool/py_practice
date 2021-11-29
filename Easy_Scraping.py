import requests
import urllib
import time
from bs4 import BeautifulSoup  # 导入解析库


# # 在url后加/robots.txt查阅网站spider文档
# response = requests.get('https://baike.baidu.com/')  # 使用requests.get()函数获取url源代码
# baidu_soul = BeautifulSoup(response.text,'html.parser')  # 使用BeautifulSoup进行解析
#
# print(baidu_soul.title)  # 输出title
# print(baidu_soul.p)  # 输出段落

start_url = 'https://en.jinzhao.wiki/wiki/Special:Random'
target_url = 'https://en.jinzhao.wiki/wiki/Philosophy'
crawler_log = [start_url]

def crawl(search_history, target_url, max_crawl= 5):
    if search_history[-1] == target_url:
        return False
    elif len(search_history) > max_crawl:
        return False
    elif search_history[-1] in search_history[:-1]:
        return False
    else:
        return True


def find_first_link(url):
    response = requests.get(url)
    wiki_soup = BeautifulSoup(response.text, 'html.parser')
    content_div = wiki_soup.find(id='mw-content-text').find(class_='mw-parser-output')
    name_link = None
    for element in content_div.find_all('p', recursive=False):
        if element.find('a', recursive=False):
            name_link = element.find('a', recursive=False).get('href')
            break
    first_link = urllib.parse.urljoin('https://en.jinzhao.wiki', name_link)
    return first_link

"""
    proxies = {"http": "http://d91.v2s4.2223.pub:8080", "https": "https://d91.v2s4.2223.pub:8080"}
    requests库可以设置代理服务器
"""

while crawl(crawler_log, target_url):
    print(crawler_log[-1])
    crawler_log.append(find_first_link(crawler_log[-1]))
    if not find_first_link(crawler_log[-1]):
        print('There is no first link')
        break
    time.sleep(0.1)