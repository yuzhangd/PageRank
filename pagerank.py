# input: graph of the web pages (a dict)
# output: pagerank values and rank of the web pages
import numpy as np

# 读取page_index
file = open('pages_index.txt')
page_index_txt = file.read()
page_index = eval(page_index_txt)
file.close()


# 读取网页graph
file = open('web_graph.txt')
graph_txt = file.read()
graph = eval(graph_txt)
file.close()

pank_of_pages = {}

def pagerank(graph):
    # build the original transition matrix H
    # 这里需要多所有的页面进行排序
    n = len(page_index)
    H = np.zeros((n, n))

    for page in page_index.keys(): # 这里遍历的时候，需要去page_index里所有的page
        row_number = page_index[page] # 这里作为矩阵的行值

        # 由于爬虫设置的原因，这里有大量的page会没有outlink
        # 如果一个web page没有outlink，对应的index一整行，赋值为0
        if page not in graph.keys() or len(graph[page]) == 0:
            H[[row_number], :] = 0
        else:
            outlinks = graph[page] # 对4号页面来说，有27个outinks
            for outlink in outlinks:
                column_number =  page_index[outlink] # 作为矩阵的列值
                num_of_one_link = outlinks.count(outlink)
                H[row_number][column_number] = num_of_one_link / len(outlinks)
    # build S based on H, to address dangling nodes 
    a = np.zeros((n, n))
    for i in range(n):
        if np.all(H[i] == 0):
            a[[i],:] = 1 # 这里的代码要再看一下是否正确

    S = H + a / n

    # build the Google matrix based on S
    
    alpha = 0.85
    G = alpha * S + np.ones((n, n)) * (1 - alpha)/n

    # iteration
    rank = np.full(n, 1/n)

    iteration = 5
    for _ in range(iteration):
        rank = np.dot(rank, G)

    # 定义函数，通过index，查询网页
    def get_key(dict, value):
        return [k for k, v in dict.items() if v == value]

    # 将网页与它的pagerank值通过一个dict联系起来
    for i in range(n):
        page = get_key(page_index, i)
        pank_of_pages[page[0]] = rank[i]

    print(pank_of_pages)
    return pank_of_pages

pagerank(graph)


