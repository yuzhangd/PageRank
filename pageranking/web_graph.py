from bs4 import BeautifulSoup
import re
from get_html import get_html

# 一个字典，key为一个网页，value为key的网页指向的网页
# 可以将网页间的连接关系理解为一个图，因此这里变量取名为graph
graph = {}

# 爬虫的起始网页，爬虫程序将以此为起点，爬取网页
# 搜索引擎中通常为设置多个起始网页，此处做了简化，只设置了一个，可以设置多个
# 实际的搜索引擎通常只会爬取整个互联网的一小部分网页（但这个数量也已经很惊人）

seed_urls = ['https://introcs.cs.princeton.edu/python/home/']

# 输入一个网页，获取这个网页指向的网页清单
def find_outlinks(url):
    outlinks =[]
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://")}):
        outlinks.append(link.get('href'))
    return outlinks


# 这里采取了一种建议的爬虫策略。即首先获取起始网页A所指向的网页B(注：B是多个网页组成的一个list)
# 然后再爬取B所指向的网页C。

def build_the_graph(url):
    url = url
    # 获取起始网页指向的网页清单
    outlinks_1 = find_outlinks(url)
    
    # 有的起始网页可能不指向其他网页，或者爬虫会失败
    if len(outlinks_1) == 0:
        print("no outlink found")
    else:
        # 起始网页为key，它指向的网页的list作为value，加入网页的graph
        graph[url] = outlinks_1

        # 爬取起始网页指向的网页所指向的下一级网页，加入graph
        for outlink_1 in outlinks_1:
            outlinks_2 = find_outlinks(outlink_1)
            if(len(outlinks_2)) == 0:
                continue
            else:
                graph[outlink_1] = outlinks_2
    print(graph)
    return(graph)
    

for url in seed_urls:
    build_the_graph(url)
