# input: query from the search box
# output: a list of sorted web pages


import streamlit as st

def get_sorted_webs(search_word):
    search_word = search_word

    # 提取每个词的index，即每个词会出现在哪些网页
    file = open('word_index.txt')
    word_index_txt = file.read()
    word_index = eval(word_index_txt)
    file.close()

    # 提取每个网页的pagerank值
    file = open('pagerank_of_pages.txt')
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


st.set_page_config(
    page_title="PageRank搜索引擎",
    page_icon=":robot:",
    layout='wide'
)



st.title('PageRank搜索引擎')

search_text = st.text_area(label="采用Google背后的PageRank算法，实现一个简易的搜索引擎。by：杜豫章。",
                           height=20,
                           placeholder="请在这里搜索...")

search_text = search_text.lower()
search_text = search_text.strip()

button = st.button("搜索", key="predict")
searched_list = []

if button:
    searched_list = get_sorted_webs(search_text)

for page in searched_list:
    st.markdown(page)

