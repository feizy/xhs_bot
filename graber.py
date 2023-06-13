import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
response = requests.get("https://www.baidu.com/", headers=headers)
# 解析
bsObj = BeautifulSoup(response.text)
# 获取 response header时间
resDate = response.headers.get('Date')
print(resDate)
# 找到热搜榜
nameList = bsObj.findAll("li", {"class": {"hotsearch-item odd", "hotsearch-item even"}})
# 添加热搜榜的内容
tests = []
for name in nameList:
    tests.append(name.getText())
# 排序
tests.sort()
for news in tests:
    news = news[1:]
    print(news)
