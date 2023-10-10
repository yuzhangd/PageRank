# 使用pagerank算法，计算所有爬取到的网页的pagerank值，即网页的重要性

import numpy as np

# 读取page_index
file = open('../data/page_index.txt')
page_index_txt = file.read()
page_index = eval(page_index_txt)
file.close()


# 读取网页graph
file = open('../data/web_graph.txt')
graph_txt = file.read()
graph = eval(graph_txt)
file.close()

rank_of_pages = {}

def pagerank(graph):
    # 具体算法说明，可参见下面这本书:Google's PageRank and Beyond: The Science of Search Engine Rankings
    # 建立初始的transition matrix H
    n = len(page_index)
    H = np.zeros((n, n))

    for page in page_index.keys():
        row_number = page_index[page] # 这里作为矩阵的行值

        # 由于爬虫设置的原因，这里有大量的page会没有outlink
        # 如果一个web page没有outlink，对应的index一整行，赋值为0
        if page not in graph.keys() or len(graph[page]) == 0:
            H[[row_number], :] = 0
        else:
            outlinks = graph[page] 
            for outlink in outlinks:
                column_number =  page_index[outlink] # 作为矩阵的列值
                num_of_one_link = outlinks.count(outlink)
                H[row_number][column_number] = num_of_one_link / len(outlinks)

    # 基于矩阵H，构建矩阵S，解决dangling nodes的问题 
    a = np.zeros((n, n))
    for i in range(n):
        if np.all(H[i] == 0):
            a[[i],:] = 1 

    S = H + a / n

    # 基于矩阵S，构建 Google matrix
    
    # 阻尼系数，设置为0.85，是个经验值。在0.85的阻尼系数下，大约100多次迭代就能收敛。
    # 当阻尼系数接近1时，需要的迭代次数会陡然增加很多，且排序不稳定。
    alpha = 0.85
    G = alpha * S + np.ones((n, n)) * (1 - alpha)/n

    rank = np.full(n, 1/n)
    
    # 迭代次数iteration设置为5次，也可以设置为其他值，值越大计算时间越长
    iteration = 5
    for _ in range(iteration):
        rank = np.dot(rank, G)

    # 定义函数，通过index，查询网页
    def get_key(dict, value):
        return [k for k, v in dict.items() if v == value]

    # 将网页与它的pagerank值通过一个dict联系起来
    for i in range(n):
        page = get_key(page_index, i)
        rank_of_pages[page[0]] = rank[i]

    return rank_of_pages

pagerank(graph)


