import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()



def main():
    intro_markdown = read_markdown_file("docs/changelog.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

if __name__ =="__main__":
    main()
