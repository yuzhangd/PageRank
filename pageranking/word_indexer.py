# 对爬取到的网页中的词进行分析，输出一个dict
# 其中，dict的key是一个词，value是这个词所出现的网页的一个list

from bs4 import BeautifulSoup
import re
from get_html import get_html

# 读取page_index
file = open('../data/page_index.txt')
page_index_txt = file.read()
page_index = eval(page_index_txt)
file.close()

urls = list(page_index.keys())

# word_index
word_index = {}


def build_word_index(url):
    texts = []

    # 读取网页的html
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

# 遍历爬取到的网页，建立词的索引
for url in urls:
    try:
        build_word_index(url)
    except:
        continue

print(word_index)
