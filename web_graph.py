
# input: an url to start crawling
# output: graph of the web pages crawled

from bs4 import BeautifulSoup
import requests
import re


graph = {}
url = 'https://introcs.cs.princeton.edu/python/home/'

  
def get_html(url):
    proxies = {
    'http':'http://61.216.185.88:60808',
    'http':'http://123.169.35.63:9999'
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.162 Safari/537.36'}
    response = requests.get(url, headers=headers, proxies=proxies)
    return response.text

# input: one url
# output: all href links(outlinks) of this url
# 这里也应该用try except
def find_outlinks(url):
    outlinks =[]
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://")}):
        outlinks.append(link.get('href'))
    return outlinks


# the crawling module gives a spider a root set of URLs to visit, instructing
# it to start there and follow links on those pages to fund new pages
# even the most comprehensive search engine indexes only a small portion of the entire web
# 爬虫可能会被access denied，出现list index out of range的错误。需要在使用request时，设置爬虫代理


def build_the_graph(url):
    url = url
    outlinks_1 = find_outlinks(url)
    
    if len(outlinks_1) == 0:
        print("no outlink found")
    else:
        graph[url] = outlinks_1
        for outlink_1 in outlinks_1:
            outlinks_2 = find_outlinks(outlink_1)
            if(len(outlinks_2)) == 0:
                continue
            else:
                graph[outlink_1] = outlinks_2
    # graph is a dict            
    return(graph)
    

build_the_graph(url)
print(graph)
