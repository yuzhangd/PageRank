# input: graph of the web pages (a dict)
# output: pagerank values and rank of the web pages
import numpy as np

# 从web_graph.txt中提取graph
file = open('web_graph.txt')
graph_txt = file.read()
graph = eval(graph_txt)
file.close()


def index_pages(graph):
    page_index = {}
    pages_from_graph = []

    # 遍历graph中的page，以及所有的outlinks
    for page in graph:
        pages_from_graph.append(page)
        for outlink in graph[page]:
            pages_from_graph.append(outlink)
   
    # 对遍历到的表，去重
    unique_pages = list(set(pages_from_graph))

    # 对去重后的web pages，编码
    index = 0
    for unique_page in unique_pages:
        page_index[unique_page] = index
        index += 1

    print(page_index)
    return page_index

index_pages(graph)


