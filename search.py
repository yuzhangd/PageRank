# 运行本程序，启动搜索引擎
# 使用如下命令运行本程序：streamlit run search.py

import streamlit as st

# 获取搜索词，输出搜索网页结果
def get_sorted_webs(search_word):
    search_word = search_word

    # 提取词的index，即词会出现在哪些网页
    file = open('./data/word_index.txt')
    word_index_txt = file.read()
    word_index = eval(word_index_txt)
    file.close()

    # 提取每个网页的pagerank值
    file = open('./data/pagerank_of_pages.txt')
    pagerank_of_pages_txt = file.read()
    pagerank_of_pages = eval(pagerank_of_pages_txt)
    file.close()

    word_in_pages = []
    # 哪些网页出现了这个搜索词
    if search_word in word_index:
        word_in_pages = word_index.get(search_word)
    else:
        print("这个搜索关键词还没有被收录，请尝试其他搜索词。")

    # 新建一个字典，key为搜索到的网页，value为网页的pagerank值
    pagerank_of_searched_pages = {}
    for page in word_in_pages:
        pagerank_of_searched_pages[page] = pagerank_of_pages[page]

    # 按value值对pagerank_of_searched_pages进行排序，按降序排列
    sorted_pagerank_of_searched_pages = sorted(pagerank_of_searched_pages.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_pagerank_of_searched_pages)
    searched_list = []
    for key in converted_dict:
        searched_list.append(key)

    return searched_list


# 设置streamlit前端页面，包括页面名称等

st.set_page_config(
    page_title="PageRank搜索引擎",
    page_icon=":robot:",
    layout='wide'
)

st.title('PageRank搜索引擎')

# 获取用户输入的搜索词
search_text = st.text_area(label="采用PageRank算法，实现一个简易的搜索引擎。访问阿里云高校计划，领取大学生专属福利: https://developer.aliyun.com/plan/student",
                           height=20,
                           placeholder="请在这里搜索...")

# 把搜索词改成小写，去掉前后空格
search_text = search_text.lower()
search_text = search_text.strip()

button = st.button("搜索", key="predict")
searched_list = []

# 用户在网页输入搜索词，点击”搜索“按键后，调用get_sorted_webs()，输出搜索结果
if button:
    searched_list = get_sorted_webs(search_text)

for page in searched_list:
    st.markdown(page)

