import streamlit as st
from investment_log.plans.target import main as target
from investment_log.ideas.target_finding import main as target_finding

"""
本页面包含金牛智道一号的投资日记

"""

# Register your pages
pages = {
    ""
    "账户投资目标": target,
    "投资想法": target_finding,
}
st.sidebar.title("投资日记")
# Widget to select your page, you can choose between radio buttons or a selectbox
page = st.sidebar.radio("选择要浏览的页面", tuple(pages.keys()))
#page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))

# Display the selected page

with st.spinner(f"Loading {page} ..."):
    pages[page]()
