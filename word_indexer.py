# input: a list of web page urls
# output: a dict, with a key as one word, and values as urls where the word appears

from bs4 import BeautifulSoup
import requests
import re

# 读取page_index
file = open('pages_index.txt')
page_index_txt = file.read()
page_index = eval(page_index_txt)
file.close()

urls = list(page_index.keys())

# words_index
word_index = {}

def get_html(url):
    proxies = {
    'http':'http://61.216.185.88:60808',
    'http':'http://123.169.35.63:9999'
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.162 Safari/537.36'}
    response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    return response.text


def build_word_index(url):
    texts = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    elements= soup.find_all('p')
    
    # 把html中p标签下出现的单词，存到一个数组texts里，每一个元素是一个单词
    for element in elements:
        text = element.get_text()
        text = re.split(r'\W+', text)
        for i in range(len(text)):
            texts.append(text[i])
        texts = list(set(texts)) # 去重

    #全部改为小写
    texts_lowercase = [element.lower() for element in texts]

    # build the graph, word_index
    for text in texts_lowercase:
        if text in word_index:
            word_index[text].append(url) #  如果这个词已经在index中了，append
        else:
            word_index[text] = [url] # 如果这个词还没有在index中，新建一个

# 这里一定要用try except，因为爬虫经常会遇到网页打不开的情况
for url in urls:
    try:
        build_word_index(url)
    except:
        continue

print(word_index)
