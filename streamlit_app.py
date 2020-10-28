import streamlit as st
from dip.data import query
from candlestick import draw_charts, split_data

st.title('投资机会分析')
stock_name = st.selectbox('选择要查看股票：',('Email', 'Home phone', 'Mobile phone'))


def load_data(sql):
    data = query(sql)
    return data

data = load_data("select name, industries , concept_indices , area_indices,"
                 " profile, main_business from zvt.stock_detail where entity_id='stock_sh_600009'")
data.columns = ['公司名称', '公司行业','概念板块','地区','公司简介','主营业务']
for cols in data:
    st.subheader(cols)
    st.write(data[cols][0])

hq_data = load_data("select \"timestamp\", \"open\", \"close\", \"high\", \"low\", \"volume\" from zvt.stock_1d_kdata where \"timestamp\" >= to_date('2010-01-01','yyyy-mm-dd') AND entity_id='stock_sh_600009'")
hq_data = hq_data.set_index('timestamp')

draw_charts(data["公司名称"][0], split_data(hq_data))
