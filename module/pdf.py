from collections import Counter
import logging
import streamlit as st

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)


# 简单方法获取范围页面的正文全文
@st.cache_data
def parse_paper_range(_pdf, start_page, end_page):
    # 页码从0开始
    start_page = start_page - 1
    end_page = end_page - 1

    all_text = []
    if start_page == end_page:
        page_content = _pdf.pages[start_page]
        all_text = page_content.extract_text()
    else:
        for page in range(start_page, end_page + 1):
            page_content = _pdf.pages[page]
            text = page_content.extract_text()
            all_text.append(text)
    return all_text
