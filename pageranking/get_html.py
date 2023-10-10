import requests
import re

def get_html(url):
    # 设置爬虫代理
    proxies = {
    'http':'http://61.216.185.88:60808',
    'http':'http://123.169.35.63:9999'
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.162 Safari/537.36'}
    response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    return response.text


