import streamlit as st
import pandas as pd
import pymysql
st.title("申万行业查询")

zvthost='123.103.74.231'
zvtuser = 'zvtreader'
zvtpasswd = 'zvtreader321'
zvtdb = 'zvt'
zvtport = 3306
conn = pymysql.connect(host=zvthost, user=zvtuser, passwd=zvtpasswd, db=zvtdb,
                       port=zvtport)

stock_code = st.sidebar.text_input('输入证券代码：', '')
exchange = st.sidebar.radio(
 '选择市场',
options=['sh', 'sz'],index=0)
stock_id = f"stock_{exchange}_{stock_code}"

if stock_code:
    sql = f"SELECT name as 行业 FROM block_stock WHERE exchange = 'swl1' and stock_id = '{stock_id}' " \
           f"union SELECT name as 二级行业 FROM block_stock WHERE exchange = 'swl2' and stock_id = '{stock_id}' " \
           f"union SELECT name as 三级行业 FROM block_stock WHERE exchange = 'swl3' and stock_id = '{stock_id}'"
    sw_data = pd.read_sql(sql, conn)
    f"一级行业: {sw_data['行业'][0]}"
    f"二级行业： {sw_data['行业'][1]}\n"
    f"三级行业: {sw_data['行业'][2]}"
else:
    sql = f"SELECT * FROM block_stock WHERE exchange = 'swl1'" \
           f"union SELECT * FROM block_stock WHERE exchange = 'swl2'" \
           f"union SELECT * FROM block_stock WHERE exchange = 'swl3'"
    sw_data = pd.read_sql(sql, conn)
    df = pd.DataFrame(columns=["股票代码","股票名称", "一级行业", "二级行业","三级行业"])
    for stock_id in sw_data.groupby("stock_id"):
        df = df.append({"股票代码":stock_id[0],"股票名称":stock_id[1]['stock_name'].iloc[0],"一级行业": stock_id[1]['name'].values[0],"二级行业": stock_id[1]['name'].values[1],"三级行业": stock_id[1]['name'].values[2]},ignore_index=True)
    st.dataframe(data=df, height=20000)

conn.close()
