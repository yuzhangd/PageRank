import os

# 爬取网页，构建网页的graph
cmd = 'python web_graph.py > ../data/web_graph.txt'
os.system(cmd)

# 对爬取到的网页做编号
cmd = 'python page_indexer.py > ../data/page_index.txt'
os.system(cmd)

# 编制词的索引
cmd = 'python word_indexer.py > ../data/word_index.txt'
os.system(cmd)

# 使用pagerank算法，计算网页的pagerank值
cmd = 'python pagerank.py > ../data/pagerank_of_pages.txt'
os.system(cmd)
