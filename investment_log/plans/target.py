from typing import Literal
import streamlit as st

def main():
    单位: Literal['年', '月', '日'] = "年"
    投资周期 = st.slider("投资周期(年)", min_value=3, max_value=10, value=3)

    st.write(
    f"""

    """
    )

if __name__ =="__main__":
    main()
